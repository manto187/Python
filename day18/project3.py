import time 
from datetime import datetime

target = input("enter time (HH:MM:SS): ")
message = input("enter reminder message: ")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    if now == target:
        print("\nreminder: ", message)
        break

    time.sleep(1)