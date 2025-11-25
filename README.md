# 📚 Book Scraper Project

A Python-based web scraping project that extracts book information from a multi-page website.
The scraper automatically navigates through all pages, collects book details, and saves the results into organized files.
# 🚀 Features
● Scrapes book titles and prices  
● Automatically detects and navigates through all pages  
● Saves data in structured format (CSV/JSON)  
● Error-handled, fast, and easy to run  
🛠️ **Technologies Used**
● Python 3
● Requests – for sending HTTP requests
● BeautifulSoup (bs4) – for parsing HTML

📁 **Project Structure**
```
book_scraper/
│── scraper.py
│── requirements.txt
│── README.md
│── data/
│     └── books.csv

```bash


▶️ **How to Run**

1.**Clone the repository**
   ```

git clone https://github.com/kebishaa/book_scraper.git
cd book_scraper
2.**Install dependencies**
```
pip install -r requirements.txt

3.**Run the scraper**
```
python scraper.py

4. The scraped data will be saved inside the data/ folder.


🚀 **Future Improvements**
●  Add image scraping
●  Export data to SQL database
●  Add a CLI interface
●  Convert into a reusable scraping package

🙌 Author
**Kibatu Mezgebu**
Passionate about automation, web scraping, and data engineering.
