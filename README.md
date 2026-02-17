# Selenium Dynamic Quotes Scraper

This project is a Selenium-based web scraper that extracts dynamically loaded quote data from a JavaScript-rendered website. It demonstrates browser automation, pagination handling, and structured data export.

## Features

- JavaScript content scraping using Selenium
- Automated browser interaction
- Dynamic pagination handling
- Quote and author extraction
- Structured data storage
- CSV export

## Technologies Used

- Python
- Selenium
- Pandas

## How It Works

1. Launches a Chrome browser using Selenium.
2. Navigates to the dynamic quotes website.
3. Extracts quote text and author information.
4. Automatically clicks through paginated pages.
5. Stores extracted data in a list.
6. Converts the data into a Pandas DataFrame.
7. Exports results to `selenium_quotes_data.csv`.

## Output

The generated CSV file contains:

- Quote
- Author

## Learning Outcomes

This project demonstrates:

- Web automation with Selenium
- Handling JavaScript-rendered pages
- Dynamic pagination logic
- Automated browser interaction
- Structured data export workflow
