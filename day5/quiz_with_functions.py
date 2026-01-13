def ask_question(a, b):
    answer = int(input(f"What is {a} + {b}? "))
    if answer == a + b:
        return True
    else:
        return False
def start_quiz():
    score = 0
    for i in range(5):
        print(f"Question {i + 1}")
        if ask_question(i + 2, i + 3):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print("Final Score:", score)
start_quiz()
