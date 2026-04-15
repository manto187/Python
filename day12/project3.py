import random

questions = [
    ("2+2", "4"),
    ("5*3", "15"),
    ("10-6", "4"),
    ("9/3", "3")

]

score = 0

for _ in range(3):
    q, ans = random.choice(questions)

    user = input(f"{q} = ")

    if user == ans:
        print("correct")
        score +=1

    else:
        print("wrong")

print("your final score is", score)
    