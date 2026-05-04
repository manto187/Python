import requests 

API_KEY = "fe409d1e35e07c01759d22e7f8d732b1"
city = input("enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")
else:
    print("city not found")