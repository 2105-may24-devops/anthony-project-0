'''
    File name: DataZero.py
    Author: Anthony M. Jarvis / @iamjarvi
    Date created: 6/1/2021
    Date last modified: 6/3/2021
    Python Version: 3.9
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request

# Permission Check Function
def url_check(input_url):
    
    # Get input URL string. Urlparse chunks the address into Scheme, Netloc, Path, Params, Query, Fragment.
    
    url = str(input_url)

    parsed_url = urlparse(url)
    scheme = str(parsed_url.scheme)
    netloc = str(parsed_url.netloc)
    path = str(parsed_url.path)

    # Ammend file with 'robots.txt'. This is a file--most websites have--that list User-Agent permissions
    # for scraping the data on their page.

    robots_url = str(f"{scheme}://{netloc}/robots.txt")
    
    # Using urllib's request; get that robot.txt.

    robots_file = urllib.request.urlopen(robots_url)
      
    # Decode the requested file and store it.

    for line in robots_file:
        decoded_file = line.decode("utf-8")

    # Check for Permissions for the path we're going to scrape.  
    # Currently (Red = Path Not Allowed, Green = Path Allowed)
    # !! More stringent checks go here !!

    permission_str = f"Disallow: {path}"      

    # Give the user a level of Risk.    
    if permission_str in decoded_file:
        print("Red") 
    else:
        print("Green")

    return url, netloc

# Scraper Function - More details to come.
    
def url_scrape(a, b):

    url = a
    netloc = b

    netloc.replace('.', '-')
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    # Get the table.

    table = soup.find('table')

    headers = []

    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    df = pd.DataFrame(columns = headers)

    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data

    print("Scraping successful!")

    # Saving the file

    download = input("Would you like to download this data? y/n ")

    if download == 'y':
        import time
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        df.to_csv(f"{netloc}_{timestr}")
        print('Save successful!')
    else:
        print("Here's a snapshot, then.")
        print(df)


# Enter the program
if __name__=="__main__":

    print("Welcome to Data Zero!\n")
    url_checked, netloc_checked = url_check(input_url=input("Input a url: \n"))

    print("Scrape this page?\n")
    answer = input('y/n\n')

    if answer == 'y':
        url_scrape(url_checked, netloc_checked)