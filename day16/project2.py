import json 

FILE = "quiz_data.json"

# load questions 
def load_questions():
    try:
        file = open(FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []
    
# save questions 
def save_questions(data):
    file = open(FILE, "w")
    json.dump(data, file)
    file.close()

# add new question
def add_question():
    question = input("enter question: ")

    options = []
    print("enter 3 options: ")
    for i in range(3):
        opt = input("option" + str(i+1)+ ":")
        options.append(opt)

    answer_index = int(input("enter correct option number(1-3): ")) -1

    data = load_questions()

    q = {
        "question": question, 
        "options": options,
        "answer": options[answer_index]
    }
    data.append(q)
    save_questions(data)
    print("questions added successfully")

# take quiz 
def take_quiz():
    data = load_questions()

    if len(data) ==0:
        print("no questions found")
        return
    score = 0

    for q in data:
        print("\n" + q["question"])

        i = 1
        for opt in q["options"]:
            print(i, opt)
            i = i+1
        try:
            choice = int(input("your ans: "))-1

            if q["options"][choice] == q["answer"]:
                print(("correct"))
                score =score+1
            else:
                print("wrong! correct answer is: ", q["answer"])
        except:
            print("\nFinal score: ", score, "/", len(data))

# view all questions
def view_questions():
    data = load_questions()

    if len(data) ==0:
        print("no questions found")
        return 
    
    i = 1
    for q in data:
        print("\nquestion", i, ":", q["question"])
        print("answer:", q["answer"])
        i = i+1

# main menu
while True:
    print("\n1.add question")
    print("2.take quiz")
    print("3.view questions")
    print("4.exit")

    choice = input("enter your choice: ")

    if choice == "1":
        add_question()
    elif choice == "2":
        take_quiz()
    elif choice == "3":
        view_questions()
    elif choice == "4":
        break
    else:
        print("invalid choice")