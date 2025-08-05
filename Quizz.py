import re
import random

question = [

     {"question":'What will this code output? \n"print(type("Hello"))"',
    "options": ["A. <type 'text'>", "B. <class 'string'>", "C. <class 'str'>", "D. <str>"],
    "answer": "C"},

    {"question": 'Which data structure does not allow duplicate values?',
    "options": ["A. Dictionary", "B. Set", "C. List", "D. Tuple"],
    "answer": "B"},

    {"question": 'What will be the output of this code?'  ' \na = [1, 2, 3]'  '\na[1]',
    "options": ["A. 1", "B. 2", "C. 3", "D. Error"],
    "answer": "B"},

    {"question": "What is the output of the code below?  \nprint(\"7\" + \"3\")",
    "options": ["A. 73", "B. 10", "C. 7 + 3", "D. Error"],
    "answer": "A"},

    {"question": "In Object Oriented Programming(OOP), what is Encapsulation?",
    "options": ["A. Combining data and methods into a single unit",
     "B. Breaking a program into smaller pieces",
     "C. Creating multiple methods with the same name but different parameters",
     "D. Hiding internal details of an object and exposing only the necessary parts."],
    "answer": "D"},

    {"question": "Which of the following is NOT a loop structure?",
    "options": ["A. do...while", "B. for", "C. loop", "D. while"],
    "answer": "C"},

    {"question": "What is the result of this?\n x = [1, 2, 3]\n x.append([4, 5])\n print(x)",
    "options": ["A. [1, 2, 3, 4, 5]", "B. [1, 2, 3, [4, 5]]", "C. [4, 5, 1, 2, 3]", "D. Error"],
    "answer": "B"},

    {"question": "Which of the following languages is primarily used for Data analysis and Machine Learning?",
    "options": ["A. Java", "B. C++", "C. HTML", "D. Python"],
    "answer": "D"},

    {"question": 'In python, what does len("Hello") return?',
    "options": ["A. 4", "B. 5", "C. 6", "D. Error"],
    "answer": "B"},

    {"question": "Which of the following defines recursion?",
    "options": ["A. A function that never ends",
     "B. A program that compiles itself",
     "C. A loop that runs forever",
     "D. A function that calls itself"],
    "answer": "D"}

    # Feel free to replace or add more questions here.
]


score = 0

print("=== Quiz Game ===")

def ask_questions(q_num, question, options, correct_answer):
    global score
    print(f"\n{q_num}. {question}")
    for option in options:
        print(option)
        
    while True:
        user_input = input("Enter Answer: ").strip().upper()
        if re.fullmatch('[A-D]', user_input):
           if user_input == correct_answer:
               print("Correct!")
               score += 1
               break
           else:
               print(f"Incorrect - Correct answer is {correct_answer}")
               break
        else:
            print("Invalid input, please enter (A, B, C, D)")


while True:

    score = 0
    selected_question = random.sample(question, len(question))

    for i, q in enumerate(selected_question, start=1):
        ask_questions(i, q["question"], q["options"], q["answer"])


    final_score = (score / len(question)) * 100  # Used norma division incase you'd like a floating point percentage value
    print("Thank you for attempting the quiz.")
    print(f"Your final score is {final_score}%")


    retry = input("Would you like to try again? (yes/no) ").strip().upper()
    if retry != 'YES':
        print("Thank you for playing")
        print("Exiting . . ...")
        print("Exited successfully")
        break

            

