import requests 

url = "https://api.coingecko.com/api/v3/simple/price"

params ={
    "ids": "bitcoin", 
    "vs_currencies": "pkr"
}

response = requests.get(url, params=params)
data = response.json()

print("bitcoin price: ", data["bitcoin"]["pkr"], "PKR")