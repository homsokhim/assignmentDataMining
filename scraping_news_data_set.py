import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
# url = 'https://edition.cnn.com/business'
# url = 'https://edition.cnn.com/politics'
# url = 'https://edition.cnn.com/world'
# url = 'https://edition.cnn.com/health'
url = 'https://edition.cnn.com/entertainment'
response = requests.get(url)
response.raise_for_status()

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <span> elements with class 'container__headline-text'
span_elements = soup.find_all('span', class_='container__headline-text')

# Find all <h1> elements with class 'headline__text'
h1_elements = soup.find_all('h1', class_='headline__text')

# Create a list to store the extracted data
data = []

# Extract the text and category from <span> elements
for span in span_elements:
    title = span.text.strip()
    category = span.parent.parent.find('span', class_='metadata__category')
    data.append({'Title': title, 'Category': category})

# Extract the text and category from <h1> elements
for h1 in h1_elements:
    title = h1.text.strip()
    category = h1.parent.parent.find('span', class_='metadata__category')
    data.append({'Title': title, 'Category': category})

# Export the data to a CSV file
filename = 'cnn_world_news_entertainment.csv'
fields = ['Title', 'Category']

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f'Data has been scraped and saved to {filename}.')