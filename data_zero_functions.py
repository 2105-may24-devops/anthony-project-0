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
import time
from pathlib import Path

# Permission Check Function
def url_check(input_url):
    
    # Get input URL string. Urlparse chunks the address into Scheme, Netloc, Path, Params, Query, Fragment.
    
    url = str(input_url)

    parsed_url = urlparse(url)
    scheme = str(parsed_url.scheme)
    netloc = str(parsed_url.netloc)
    path = str(parsed_url.path)
    risk_level = 0;

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
         
        risk_level = 'Red'
        print("\n")
        print(f"Your risk level is {risk_level}! This site would prefer to keep the data to themselves.")
        
    elif robots_file == 0:
        risk_level ='Yellow'
        print("\n")
        print(f"Your risk level is {risk_level}! This site has no permissions to speak of...")
        
    else:
        risk_level = 'Green'
        print("\n")
        print(f"Your risk level is {risk_level}! Free numbers!")
    
    
    return url, netloc, risk_level, path

# Scraper Function - More details to come.
    
def url_scrape(a, b, c):

    url = a
    netloc = b
    path = c
    scraped = True
    saved = False

    netloc.replace('.', '-')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='lxml')

    # Get the table.
    try:
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

        print("!!!!   Scraping successful  !!!!\n\n")
    
        # Saving file and creating subfolders.
        print("Would you like to save this data?")
        download = input("Yes (y) or No (n)\n\n")

        if download == 'y':

            #Create folder, using the netloc as a name.
            path = Path(f"./saved_data/{netloc}/{path}")
            path.mkdir(parents=True, exist_ok=True)
            
            # Save File
            timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
            df.to_csv(f"{path}/{netloc}_{timestr}")
            print('!!!!    Save successful    !!!!\n\n')
            saved = True
        else:
            print("....    Here's a snapshot, then    ....\n\n")
            print(df)
            saved = False
    except:
        print("No tabular data found. Try a different page!")

    return scraped, saved

# call history function

def history(history):
    
	from csv import writer


	# Takes the last scraped url into the function for logging.
	# It should record the name of the site, the time, and whether or not the user saved or viewed the data.

	log_data = history
	log_data.append(time.strftime("%d-%m-%Y_%H:%M:%S"))

	# Opens data-histroy.csv, if it doesn't exist creates it.
	
	with open('data-history.csv', 'a+') as f_object:

		writer_object = writer(f_object)

		writer_object.writerow(log_data)

		f_object.close()

# Rescraper Function

def rapid_scraper(input):

    url = input

    parsed_url = urlparse(url)
    scheme = str(parsed_url.scheme)
    netloc = str(parsed_url.netloc)
    path = str(parsed_url.path)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='html')

    # Get the table.
    try:
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

        print("!!!!    Scraping Successful    !!!!")
    
        #Create folder, using the netloc as a name.
        path = Path(f"./saved_data/{netloc}/{path}")
        path.mkdir(parents=True, exist_ok=True)

        # Saving the file
            
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        df.to_csv(f"rapidtestscrape")
        print('!!!!    Save successful    !!!!')
        saved = True

    except:
        print("!!!!   No tabular data found    !!!!")
    
