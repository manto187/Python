def update_highscore(new_score):
    try:
        with open("highscore.txt", "r") as file:
            current_high = int(file.read())
    except (FileNotFoundError, ValueError):
        current_high = 0

    if new_score > current_high:
        print(f"new high score {new_score}")
        with open("highscore.txt", "w") as file:
            file.write(str(new_score))

    else:
        print(f"keep trying! high score is still {current_high}")

update_highscore(85)