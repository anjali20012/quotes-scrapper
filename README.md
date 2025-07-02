# Quotes Scraper 📝

This Python project scrapes inspirational quotes from a *JavaScript-rendered website* using *Selenium* and *BeautifulSoup. The data is then saved into a **PostgreSQL database* and exported to a *CSV file*.

---

## 🚀 Features

- Uses Selenium WebDriver to handle dynamic content
- Parses HTML using BeautifulSoup
- Extracts quotes and author names
- Saves data to:
  - PostgreSQL database
  - CSV file (output.csv)

---

## 📂 Folder Structure
quotes_scraper_project/ ├── scrapper.py ├── requirements.txt ├── .env ├── output.csv └── chromedriver.exe

---

## 💻 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/anjali20012/quotes-scrapper.git
cd quotes-scrapper

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Set up .env with your PostgreSQL DB credentialsRun the scraper

python scrapper.py


---

🛠️ Technologies Used

Python

Selenium

BeautifulSoup

PostgreSQL

CSV

dotenv



---

📤 Output Example

A sample CSV file (output.csv) is generated with this structure:

Quote	Author

“Life is what happens ...”	John Lennon
“Be yourself ...”	Oscar Wilde


