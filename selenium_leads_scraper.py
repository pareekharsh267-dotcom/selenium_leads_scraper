from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

data = []

driver.get("https://quotes.toscrape.com/js/")

time.sleep(3)

while True:
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text

        data.append({
            "Quote": text,
            "Author": author
        })

    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next →")
        next_button.click()
        time.sleep(2)
    except:
        break

driver.quit()

df = pd.DataFrame(data)
df.to_csv("selenium_quotes_data.csv", index=False)

print("Scraping completed successfully!")