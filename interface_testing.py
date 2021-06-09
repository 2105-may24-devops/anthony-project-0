from tkinter import *

# Define thie root window.

root = Tk()
root.title("DataZero Webscraping Tool")
root.geometry("600x200")


# Create Widgets
scrape_frame = LabelFrame(root, text="Check and Scrape", padx=75, pady=30)

url_entry = Entry(scrape_frame, width=50)
def get_text():
	entry = url_entry.get()
	return entry
scrape_button = Button(scrape_frame, text="Scrape", command=get_text())
url = get_text()
url_result = Label(scrape_frame, text=url).grid(row=2, column=1)
status = Label(root, text="ready", bd=1, relief=SUNKEN, anchor=E)



# Put widgets onto the screen.

scrape_frame.grid(row=0, column=0, padx=15, pady=10)

url_entry.grid(row=0, column=1, padx=5, pady=5)
scrape_button.grid(row=1, column=1, padx=5, pady=10)
status.grid(row=1, column=0, padx=1, sticky=E+W)

# Create an event loop.


root.mainloop()