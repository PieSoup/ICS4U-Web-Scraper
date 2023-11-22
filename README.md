# ICS4U-Web-Scraper
## Overview:
This Python script is designed to scrape information about speedruns from the website "speedrun.com" for a specific game called "The Legend of Zelda: Twilight Princess HD" (abbreviated as TOTK). The script utilizes the BeautifulSoup library for web scraping, the requests library for making HTTP requests, and the csv library for working with CSV files.
## Functionality:
### Importing Libraries:
The script starts by importing the necessary libraries: BeautifulSoup, requests, and csv.
### Scrape Function:
The main function in the script is named scrape, which takes a URL (source) as input.
The function performs the following steps:
Makes an HTTP GET request to the specified URL and retrieves the HTML content.
Parses the HTML content using BeautifulSoup with the 'lxml' parser.
Finds all HTML elements with the tag "table" and the specified class "w-full whitespace-nowrap," which contains speedrun entries.
Iterates through each table element and further iterates through each table row / speedrun within it.
Extracts relevant information such as username, country, version, and time for each speedrun entry.
Cleans and processes the extracted data.
Writes the extracted data to a CSV file.
### URLs:
Create a list of URLs to scrape as games usually have multiple pages to fit all of the runs. Loop through each URL and run the scrape function on it
### CSV File:
The script opens a CSV file named 'data.csv' in write mode and creates a CSV writer object.
Writes a header row to the CSV file with column names: 'Name', 'Country', 'Time', 'Version'.
## Usage:
Execute script using a python environment
The script will generate a 'data.csv' file with all of the necessary data
