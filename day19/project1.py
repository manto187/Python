import requests 
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("failed to fetch page")
        return 
    
    soup = BeautifulSoup(response.text, "html.parser")

    # title
    title = soup.find("h1").text
    print(f"\ntitle: {title}\n")

    # paragraphs 
    paragraphs = soup.find_all("p")
    print("content: \n")
    for p in paragraphs[:5]:
        print(p.text.strip())
        print()

    # links
    print("\nlinks: \n")
    for p in paragraphs[:5]:
        links = p.find_all("a")
        for link in links[:10]:
            href = link.get("href")
            if href:
                print(href)

scrape_wikipedia("https://en.wikipedia.org/wiki/Web_scraping")