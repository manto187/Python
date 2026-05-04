from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.com/news"

try:
	req = requests.get(url, timeout=10)
	req.raise_for_status()
except requests.exceptions.RequestException as err:
	print(f"Failed to fetch {url}: {err}")
else:
	soup = BeautifulSoup(req.text, "html.parser")
	print(soup.title.string if soup.title else "No title found")