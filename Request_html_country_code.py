import requests
from bs4 import BeautifulSoup

def get_table_code():
    # URL of all the country codes 
    url = "https://countrycode.org/"
    response = requests.get(url)
    
    # Create an object BeautifulSoup to analyze the web page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table for the class, you can see the table class doing an inspection in the web page
    table = soup.find('table', class_='table table-hover table-striped main-table')
    
    country_info=[]
    countries_info=[]
    
    #Go to the rows table
    rows = table.find_all('tr')
    for row in rows:
        #Go to each cell on the row
        cells = row.find_all('td')
        for cell in cells:
            # Save all the country info in a list (a single row has all the info of the country) 
            country_info.append(cell.text)
        #Save the country info in another list, this list has all the countries info
        countries_info.append(country_info)
        country_info=[]
    return countries_info[1:]