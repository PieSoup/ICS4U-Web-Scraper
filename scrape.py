# Import necessary libraries for web scraping (BeautifulSoup), making HTTP requests (requests), and working with CSV files (csv).
from bs4 import BeautifulSoup
import requests
import csv

# Define a function named "scrape" that takes a URL as input.
def scrape(source):

    # Make an HTTP GET request to the specified URL and retrieve the HTML content.
    source = requests.get(source).text
    # Create a BeautifulSoup object to parse the HTML content using the 'lxml' parser.
    soup = BeautifulSoup(source, 'lxml')

    # Find all HTML elements with the tag "table" and the specified class "w-full whitespace-nowrap".
    # Each run entry is within this table
    runs = soup.findAll("table", {"class": "w-full whitespace-nowrap"})

    # Iterate through each 'table' element found.
    for run in runs:
        # Find all 'tr' (table row) elements within the current 'table' element.
        # Each one of these rows is a unique speedrun
        rows = run.findAll('tr')
        # Iterate through each run.
        for row in rows:

            # Find the 'a' (anchor) element with the class "x-username" within the current speedrun.
            username_element = row.find('a', class_='x-username')
            # Find all 'a' elements with the classes "px-1.5 py-1" within the current speedrun.
            time_element = row.find_all('a', class_="px-1.5 py-1")
            version_element = row.find_all('a', class_="px-1.5 py-1")
            country_element = ''

            # Initialize variables to store extracted data.
            username = ''
            country = ''
            version = ''
            time = ''
            hours = '0'
            minutes = '00'
            seconds = '00'

            # Check if the 'username_element' exists.
            if username_element:
                # Find the 'img' element within the 'username_element' to extract the 'alt' attribute.
                # This attribute stores the name of the country the flag image represents
                country_element = username_element.find('img', alt=True)
                # Extract the text content of the 'span' element within the 'username_element' (username of the runner).
                username = username_element.span.text
            
            # Check if the 'country_element' exists.
            if country_element:
                # Extract the 'alt' attribute of the 'country_element' to get the name.
                country = country_element.get('alt', '')
                # Check if there are multiple values separated by commas in the 'country'.
                if len(country.split(', ')) > 1:
                    # Extract the last value after splitting by commas as this is the country name.
                    # Some of the entries also had provinces / states, and I just want the country
                    country = country.split(', ')[len(country.split(', ')) - 1]

            # Check if the 'version_element' exists.
            if version_element:
                # Extract the fifth element from the 'version_element' list and then extract the text content.
                version_element = version_element[4] # The fifth element is where the version is stored
                version = version_element.span.text

            # Check if the 'time_element' exists.
            if time_element:
                # Extract the second element from the 'time_element' list and then extract the text content.
                time_element = time_element[1] # The second element is where the time is stored
                time = time_element.span.text
                # Remove non-digit characters from 'time' but keep spaces.
                time = ''.join(c for c in time if c.isdigit() or c == ' ')
                
                # Initialize variables to store hours, minutes, and seconds.
                # The split function separates the string into different parts where there are spaces
                if(len(time.split()) > 2):
                    hours = time.split()[0]
                    minutes = time.split()[1]
                    seconds = time.split()[2]
                else:
                    minutes = time.split()[0]
                    seconds = time.split()[1] 

            # Check if both 'username' and 'time' are not empty.
            if username != '' and time != '':
                # Write a new row to the CSV file with the extracted data.
                writer.writerow([username, country, f'{hours.zfill(2)}:{minutes}:{seconds}', version])

# List of URLs to scrape.
pages = ["https://www.speedrun.com/totk", "https://www.speedrun.com/totk?h=Any-pre-v1-2-1&page=2&x=w20mopzk-rn1g4gdn.14ooyy0q"]

# Open a CSV file in write mode and create a CSV writer object.
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row to the CSV file.
    writer.writerow(['Name', 'Country', 'Time', 'Version'])
    # Iterate through each URL in the 'pages' list and call the 'scrape' function.
    for page in pages:
        scrape(page)
