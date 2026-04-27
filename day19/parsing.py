from bs4 import BeautifulSoup
import requests 

url = "htts://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.txt, "html.parser")
print(soup.title.text)


# find one heading 
soup.find("h1")

# find all
soup.find_all("p")

# by class 
soup.find("div", class_="content")

# by id 
soup.find(id="main")