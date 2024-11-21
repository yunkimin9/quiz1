
users = {}
questions = {
    "DSA": [
        {"question": "What does DSA stand for?", "options": ["Data Science and Analysis", "Data Structures and Algorithms", "Data Storage and Analysis", "Dynamic System Analysis"], "answer": 1},
        {"question": "Which of these is a linear data structure?", "options": ["Tree", "Graph", "Array", "Hash Table"], "answer": 2},
        {"question": "What is the time complexity of binary search?", "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "answer": 1},
        {"question": "Which data structure uses LIFO principle?", "options": ["Queue", "Stack", "Array", "Linked List"], "answer": 1},
        {"question": "Which algorithm is used to solve the shortest path problem?", "options": ["DFS", "BFS", "Dijkstra's Algorithm", "Merge Sort"], "answer": 2}
    ],
    "DBMS": [
        {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Backup Management System", "Dynamic Base Management System", "Direct Base Management System"], "answer": 0},
        {"question": "Which of the following is a type of database?", "options": ["Flat File", "Hierarchical", "Relational", "All of the above"], "answer": 3},
        {"question": "What is SQL?", "options": ["Structured Query Language", "System Query Language", "Standard Query Language", "Structured Query Loop"], "answer": 0},
        {"question": "Which one of these is used for defining relationships in DBMS?", "options": ["Foreign Key", "Primary Key", "Unique Key", "All of the above"], "answer": 0},
        {"question": "Which of the following is not a DBMS?", "options": ["MySQL", "PostgreSQL", "SQLite", "Excel"], "answer": 3}
    ],
    "Python": [
        {"question": "Which of the following is a valid Python variable name?", "options": ["1variable", "_variable", "@variable", "$variable"], "answer": 1},
        {"question": "Which of the following is used for comments in Python?", "options": ["//", "#", "/* */", "--"], "answer": 1},
        {"question": "Which data type is used to store decimal numbers?", "options": ["int", "float", "str", "bool"], "answer": 1},
        {"question": "Which of the following is a Python library for data analysis?", "options": ["NumPy", "Matplotlib", "Pandas", "All of the above"], "answer": 2},
        {"question": "What is the output of 3 + 2 * 2 in Python?", "options": ["10", "7", "8", "5"], "answer": 1}
    ]
}

#  display banner
def display_banner():
    print("===================================")
    print("     Welcome to the Quiz App!")
    print("===================================")

# register a new user
def register_user():
    print("==== Registration ====")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    users[username] = password
    print("Registration successful!")

     # Save registration info to a text file
    with open("registration_info.txt", "a") as file:  # Append mode
        file.write(f"{username},{password}\n")  # Save username and password

# login user
def login_user():
    print("==== Login ====")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Try again.")
        return False

#  quiz
def take_quiz(subject):
    print(f"Starting {subject} Quiz...")
    score = 0
    wrong_answers = []
    for i, q in enumerate(questions[subject]):
        print(f"Q{i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j}. {option}")
        answer = int(input("Enter the number of the correct answer: "))
        if answer == q['answer']:
            score += 1
        else:
            wrong_answers.append((q['question'], q['options'][q['answer']]))
    return score, wrong_answers 


# results
def display_results(score, total, wrong_answers ):
    print(f"\nYou got {score} out of {total} questions correct!")
    if score == total:
        print("Excellent! Full marks!")
    elif score >= total // 2:
        print("Good job!")
    else:
        print("Better luck next time!")

    if wrong_answers:
        print("\nHere are the correct answers for the questions you got wrong:")
        for question, correct_answer in wrong_answers:
            print(f"Question: {question} - Correct Answer: {correct_answer}")


# exit or go back to the quiz section
def exit_or_continue_quiz():
    choice = input("\nDo you want to (1) Exit Quiz, or (2) Return to Quiz Section? (1/2): ")
    return choice

# Main 
def main():
    display_banner()
    
    while True:
        choice = input("Do you want to (1) Register, (2) Login, (3) Exit: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                while True:
                    print("==== Welcome to the Quiz Section ====")
                    subject = input("Choose a subject (1)DSA,(2) DBMS, (3)Python: ")
                    
                    if subject in questions:
                        score, wrong_answers = take_quiz(subject)  #  score and wrong answers
                        display_results(score, len(questions[subject]), wrong_answers)
                        user_choice = exit_or_continue_quiz()
                        if user_choice == "1":
                            print("Exiting quiz...")
                            break  # Exit the quiz section and return to the main menu
                        elif user_choice == "2":
                            continue  # Return to the quiz section
                        else:
                            print("Invalid choice. Returning to quiz section.")
                            continue 
                    else:
                        print("Invalid subject selected. Please try again.")
            else:
                print("Login failed.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
