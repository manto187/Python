users = {}

n = int(input("how many users do you want to add?...."))
for i in range(n):
    username = input("enter username: ")
    password = input("enter password: ")
    users[username] = password
print("----Login system----")
 
login_user = input("enter username: ")
login_pass = input("enter password: ")

if login_user in users and users[login_user] == login_pass:
    print("login successful!")
else:
    print("invalid username or password")
