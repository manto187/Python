from bs4 import BeautifulSoup
import requests 

url = "htts://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.txt, "html.parser")
print(soup.title.text)