import time 

def countdown(seconds):
    while seconds>0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -=1

print("study time (25 mins)")
countdown(25*60)

print("\nbreak time (5 mins)")
countdown(5*60)

print("\ncycle complete")