import requests 

url =  "http://ip-api.com/json/"

response = requests.get(url)

data = response.json()

print("country:", data["country"])
print("city:", data["city"])
print("ISP:", data["isp"])