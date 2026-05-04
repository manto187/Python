from datetime import datetime 

def journal_logger():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"   Journal Entry   {date_str}     ")

    mood = input("how are you feeling today?")
    entry = input("write your thoughts: ")

    try:
        with open("journal.txt", "a") as file:
            file.write(f"date: {date_str}\n")
            file.write(f"mood: {mood}\n")
            file.write(f"entry: {entry}\n")
            file.write("-" * 20+"\n")
        print("entry saved successfully")
    except Exception as e:
        print(f"failed to save: {e}")

journal_logger()