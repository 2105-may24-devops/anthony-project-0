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
        print(risk_level)

    elif robots_file == 0:

        risk_level('Yellow')
        print(risk_level)

    else:
        
        risk_level = 'Green'
        print(risk_level)

    return url, netloc, risk_level

# Scraper Function - More details to come.
    
def url_scrape(a, b):

    url = a
    netloc = b
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

        print("Scraping successful!")
    
        # Saving the file

        download = input("Would you like to download this data? y/n ")

        if download == 'y':
            
            timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
            df.to_csv(f"{netloc}_{timestr}")
            print('Save successful!')
            saved = True
        else:
            print("Here's a snapshot, then.")
            print(df)
            saved = False
    except:
        print("No tabular data found.")

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
    import os

    url = input

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

        os.system("echo Scraping Successful!")
    
        # Saving the file
            
        timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        df.to_csv(f"rapid-scrape_{timestr}")
        print('Save successful!')
        saved = True
    except:
        os.system("echo No tabular data found!")
    
