print("welcome to the basic math quiz game!")
score = 0 
total_questions = 3
for i in range(total_questions):
    print(f"Question {i+1}: What is {i+2} + {i+3}?")
    answer = int(input("Your answer: "))
    if answer == (i+2) + (i+3):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
print(f"Your final score is {score} out of {total_questions}.")