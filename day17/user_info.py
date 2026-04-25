import requests 
username = input("enter your username: ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("name: ", data["name"])
    print("public repos:", data["public_repos"])
else:
    print("user not found")