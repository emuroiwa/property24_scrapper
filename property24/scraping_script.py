import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Find all headings
        headings = soup.find_all('h1')
        return [heading.text for heading in headings]
    else:
        return None
