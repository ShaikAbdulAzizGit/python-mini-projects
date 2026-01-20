import random
def run_quiz(quiz_questions):
    print("Welcome to simple quiz game ")
    question_no=1
    score=0
    for question in quiz_questions:
        print(f"Question no : {question_no}")
        print(question[0])
        print(f"A. {question[1]}")
        print(f"B. {question[2]}")
        print(f"C. {question[3]}")
        print(f"D. {question[4]}")
        question_no+=1
        while True:
            user_selection=input("Enter the option ").strip().upper()
            valid_option={"A","B","C","D"}
            if user_selection not in valid_option:
                print("Unexpected selection please try again choosing correct option")
            else:
                break
        choice_map={
            "A":1,
            "B":2,
            "C":3,
            "D":4
        }
        if choice_map[user_selection]==question[5]:
            print(f"You are correct : The correct option is {question[question[5]]}")
            score+=1
        else:
            print(f"You are incorrect : The correct option is {question[question[5]]}")
    print(f"The total score is : {score} out of {len(quiz_questions)}")


quiz_questions = [
    ["What is the output of 2 + 3 * 4?", "14", "20", "24", "10", 1],
    ["Which data type is immutable in Python?", "List", "Dictionary", "Set", "Tuple", 4],
    ["What keyword is used to define a function in Python?", "func", "def", "function", "define", 2],
    ["What will len('Python') return?", "5", "6", "7", "None", 2],
    ["Which of the following is a Python loop?", "for", "loop", "repeat", "do", 1],
    ["What does '==' do in Python?", "Assign value", "Compare values", "Start loop", "None of the above", 2],
    ["Which of these is not a Python data structure?", "Queue", "Tuple", "List", "Dictionary", 1],
    ["What is the output of print(type(10))?", "<class 'int'>", "<type 'int'>", "integer", "number", 1],
    ["Which method is used to add an item to a list?", "append()", "add()", "insert()", "extend()", 1],
    ["What is the result of 10 // 3?", "3.33", "3", "3.0", "Error", 2]
]

while True:
    random.shuffle(quiz_questions)
    run_quiz(quiz_questions)
    again=input("Do you want to play again ?....(Y/N)").strip().lower()
    if again !="y":
        print("Thanks for playing the game !..")
        break
    
