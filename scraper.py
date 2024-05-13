from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
from dotenv import load_dotenv
import requests
import datetime
from parser_1 import parse
import logging

logging.basicConfig(level=logging.DEBUG, filename='selenium.log')

load_dotenv()

# Creating a webdriver instance
driver = webdriver.Chrome()
# This instance will be used to log into LinkedIn
 
# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
 
# waiting for the page to load
time.sleep(5)
 
# entering username
username = driver.find_element(By.ID, "username")
 
# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys(os.getenv('USERNAME'))  
 
# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element 
# tag used here.
 
# Enter Your Password
pword.send_keys(os.getenv('PASSWORD'))        
 
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Send a GET request to the webpage
# response = requests.get(url)

print("Logged in.")

# Prepare a list to hold the data
data = []

driver.get('https://www.linkedin.com/groups/55739/members/') 

# First scroll
start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

start = time.time()
runtime = 5000  # runtime in seconds
filename = f'page_content_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.html'


try:
    # Open the file outside the loop
    
        while True:
            
            # Scroll down
            driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
            time.sleep(5)  # Wait for the page to load

            driver.execute_script(f"window.scrollTo({finalScroll}, {initialScroll - 1500})")
            time.sleep(5)

            # Capture the current state of the page
            current_src = driver.page_source
            with open(filename, 'w', encoding='utf-8') as file:
            # Write the current page source to the file
                file.write(current_src)
                print(f"File is now {os.path.getsize(filename)} bytes")

            # artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button
            try: driver.find_element(By.XPATH, "//button[contains(@class, 'scaffold-finite-scroll__load-button')]").click()
            except: print("No Button")
            # Update scroll positions
            initialScroll = finalScroll
            finalScroll += 1000

            # Check if runtime is exceeded
            end = time.time()
            print(f"Status: SCROLLING | Time: {end}")
            if round(end - start) > runtime:
                print("Finished Scrolling!")
                break
except Exception as e:
    logging.error(f"An unexpected error ocurred at {time.time()}:", exc_info=True)
finally: driver.quit()
    
parse(filename)