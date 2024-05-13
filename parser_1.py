from bs4 import BeautifulSoup
import pandas as pd

def parse (file_r):
    # Load the HTML from the saved file
    with open(file_r, 'r', encoding='utf-8') as file:  # Use the actual filename
        src = file.read()
    
    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')

    #Finite Scroll
    fs = soup.find('div', class_='scaffold-finite-scroll__content')
    #UL
    ul = fs.find('ul', class_='artdeco-list groups-members-list__results-list')
    list_items = ul.find_all('li')
    print(len(list_items))

    # scaffold-finite-scroll scaffold-finite-scroll--infinite
    
    names = []
    titles = []
    for li in list_items:
        names.append(li.find('div', class_='artdeco-entity-lockup__title ember-view').text.strip())
        titles.append(li.find('div', class_='artdeco-entity-lockup__subtitle ember-view').text.strip())

    data = zip(names,titles)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Title'])

    for col in df.select_dtypes(include=['object']):  # Assumes text columns are of type 'object'
        df[col] = df[col].str.strip().replace(r'\s+', ' ', regex=True)

    # Write the DataFrame to an Excel file
    df.to_excel('output.xlsx', index=False)