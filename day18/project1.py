import time
from datetime import datetime 

event = datetime(2026, 12, 31, 0, 0)

while True:
    now = datetime.now()
    remaining = event - now

    print("time left: ", remaining, end="\r")
    time.sleep(1)