import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 51):  # 50 pages
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Page {page} not found, stopping.")
        break

    soup = BeautifulSoup(response.text, "lxml")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        all_books.append([title, price])

   # print(f"Scraped page {page}")

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    writer.writerows(all_books)

#print(f"\nTotal books scraped: {len(all_books)}")
print("Data saved to books.csv")
