import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request

def url_check(input_url):
    
        # Get input URL string. Urlparse chunks the address into Scheme, Netloc, Path, Params, Query, Fragment.
    # Strip the url down, take the netloc and append 'robots.txt' to look for user-agent
    # permissions.

    url = str(input_url)
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    print(robots_url)
    print(parsed_url.path)
    
    robots_file = urllib.request.urlopen(robots_url)
    print(robots_file)
    
        # Search robots.txt for the path we want to scrape. If Disallowed, alert user that it would be
    # risky to proceed. Currently (Red = Path Not Allowed, Green = Path Allowed)
    
    for line in robots_file:
        decoded_file = line.decode("utf-8")
        print(decoded_file)
        
    permission_str = f"Disallow:{parsed_url.path}"      
        
    if permission_str in decoded_file:
        print("Red") 
    else:
        print("Green")

