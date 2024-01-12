import csv
import requests
from bs4 import BeautifulSoup

# URL of the news website you want to scrape
url = "https://edition.cnn.com/world"  # Replace "https://example.com/news" with the actual URL of the news website you want to scrape

# Send a GET request to the website and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements containing the titles and categories of the articles
title_elements = soup.find_all("span", class_="container__headline-text")  # Replace "h2" and "article-title" with the actual HTML tags and classes for the title elements
category_elements = soup.find_all("h1", class_="headline__text")  # Replace "span" and "article-category" with the actual HTML tags and classes for the category elements

# Create a list to store the scraped data
data = []

# Iterate over the article elements and extract the title and category
for title_element, category_element in zip(title_elements, category_elements):
    title = title_element.text.strip()
    category = category_element.text.strip()
    data.append([title, category])

# Export the data to a CSV file
csv_filename = "news_data.csv"  # Specify the desired filename for the CSV file
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Category"])  # Write the header row
    writer.writerows(data)  # Write the data rows

print(f"Data scraped successfully and saved to {csv_filename}.")