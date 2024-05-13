# LinkedIn Group Members Scraper

This Python project automates the extraction of member names and titles from a specific LinkedIn group. It leverages Selenium WebDriver for browser automation to scroll through the group's member list page, captures the dynamically loaded content, and then parses it using BeautifulSoup to extract and save the data into an Excel file.

## Features

- **Automated Browser Navigation**: Logs into LinkedIn and navigates to the group's member list.
- **Dynamic Content Handling**: Manages infinite scrolling to load all members' data.
- **Data Extraction**: Parses HTML content to extract members' names and titles.
- **Excel Output**: Saves the extracted data into an Excel spreadsheet for easy use and analysis.

## Prerequisites

To run this script, you need:

- Python 3.6 or higher
- Selenium WebDriver
- Google Chrome and ChromeDriver
- BeautifulSoup4
- pandas
- python-dotenv

## Installation

1. **Clone this repository** or download the files to your local machine.
2. **Install the required libraries** using pip:

    ```
    pip install selenium beautifulsoup4 pandas python-dotenv
    ```

3. **ChromeDriver**: Ensure that ChromeDriver is installed and its path is correctly set up in your system's PATH, or modify the script to point to its location.

## Setup

1. **Environment Variables**: Create a `.env` file in the project directory with your LinkedIn credentials:

    ```
    USERNAME=your_linkedin_email
    PASSWORD=your_linkedin_password
    ```

2. **Modify Group URL** (if necessary): Change the group URL in the script to match the LinkedIn group you are interested in.

## Usage

Run the script from the command line:

    python linkedin_scraper.py

After the script completes its execution, check the `output.xlsx` file in the project directory for the results.

## How It Works

### Login and Navigation

- The script starts by launching Chrome via Selenium and navigates to the LinkedIn login page.
- It reads the username and password from the `.env` file and logs into LinkedIn.
- After login, it navigates to the specified group members' page.

### Dynamic Scrolling and Data Capture

- Selenium script automatically scrolls through the page to load all members.
- It captures the HTML content of the page at different scroll stages and attempts to click "Show more results" if present.

### Parsing HTML

- The captured HTML content is saved to a file.
- The `parse` function is called, which uses BeautifulSoup to read the HTML file, extracts the members' names and titles, and then cleans the text data.

### Excel Output

- Extracted data is stored in a pandas DataFrame and then exported to an Excel file named `output.xlsx`.

## Script Details

### Scraper Script

    # Code snippet to illustrate browser automation
    driver = webdriver.Chrome()
    driver.get("https://linkedin.com/uas/login")
    # Login actions and navigation
    # Scrolling and data capture logic

### Parser Function

    # Code snippet to illustrate parsing logic
    def parse(file_r):
        with open(file_r, 'r', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        # Element extraction and DataFrame creation
        df.to_excel('output.xlsx', index=False)

## Customization

You can customize the script by modifying the group URL, adjusting scroll behavior, or changing how data is parsed and stored.

## Disclaimer

This script is intended for educational purposes only. Be sure to comply with LinkedIn's terms of service regarding automated access and data scraping.
