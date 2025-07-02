from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import psycopg2
import csv

import time

import os

from dotenv import load_dotenv


load_dotenv()

# Step 1: Launch Chrome and load website
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")
time.sleep(3)

# Step 2: Scrape data
soup = BeautifulSoup(driver.page_source, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
data = [(q.text.strip(), a.text.strip()) for q, a in zip(quotes, authors)]
driver.quit()

# Step 3: Connect to PostgreSQL

db_url = os.getenv("DB_URL")

conn = psycopg2.connect(db_url)
cur = conn.cursor()

# Step 4: Create table and insert
cur.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id SERIAL PRIMARY KEY,
        quote TEXT,
        author TEXT
    )
""")
for quote, author in data:
    cur.execute("INSERT INTO quotes (quote, author) VALUES (%s, %s)", (quote, author))
conn.commit()

# Step 5: Export to CSV
with open("quotes_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

cur.close()
conn.close()
print("✅ Project complete! Data saved to DB and quotes_output.csv")