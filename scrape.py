# scrape.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # ensure we notice bad responses
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text from paragraphs (you can customize this as needed)
    texts = [p.get_text() for p in soup.find_all('p')]
    return "\n".join(texts)
