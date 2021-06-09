from data_zero_functions import *

def main():

    # Declare a list to store data for logging purposes.

    history_data = []

    # Greeting, future UI stuff?
    print("------------       Welcome to Data Zero!       ----------------")
    print("***************************************************************\n\n")

    # Call the url permissions check.
    print("Enter a URL with tabular data that would like to save or view.")
    print("---------------------------------------------------------------\n\n")


    url_checked, netloc_checked, risk_level, url_path = url_check(input_url=input("Input a url: \n\n"))

    history_data.append(str(url_checked))
    history_data.append(str(risk_level))

    # Ask the user whether or not they want to scrape. Note: A Red risk-level will not prevent a user from scraping a page
    # it only lets them know whether or not it's allowed. The risk belongs to the user.

    
    answer = input("Would you like to scrape this page?\n Yes (y) or No (n)\n")


    if answer == 'y':
        url_scraped, url_saved = url_scrape(url_checked, netloc_checked, url_path)


    history_data.append(str(url_scraped))
    history_data.append(str(url_saved))
    history(history_data)

  # Enter the program
if __name__ == "__main__":
  main()