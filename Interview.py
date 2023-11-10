import os
import json
import time

def clear():
    print("\033[2J\033[H",end="")

clear()


interview_questions = [
    "Tell me about a challenging project you've worked on and how you handled it.",
    "Can you describe a situation where you had to work with a difficult team member? How did you handle it?",
    "What do you do to stay updated in your field?",
    "Give an example of a time when you had to meet a tight deadline. How did you prioritize and organize to get the work done?",
    "How do you handle feedback and criticism?"
]

def session():
    answers = []
    for question in interview_questions:
        clear()
        answers.append(input(question + " > "))

    clear()
    name = input("What is your name? > ")
    clear()
    input("You're done! [Press enter to continue] ")


    f = open("answers.json", "w+")
    contents = f.read()
    arr = []
    try:
        arr = json.loads(contents)
    except Exception:
        arr = []

    dict = {"name":name,"questions":{},"timestamp":time.time()}
    for i in range(len(interview_questions)):
        dict["questions"][interview_questions[i]] = answers[i]

    arr.append(dict)

    f.write(json.dumps(arr))
    f.close()

def view():
    f = open("answers.json", "r+")
    contents = f.read()
    arr = []
    try:
        arr = json.loads(contents)
    except Exception:
        arr = []
    
    f.close()
    if len(arr) < 1:
        clear()
        input("There are no saved answers. [Press enter to continue]")
        return 

    print("Saved answers:")
    for i in range(len(arr)):
        print(str(i) + ": " + arr[i]["name"])
    selection = input("Which would you like to view? > ")
    try:
        num = int(selection)
    except Exception:
        input("Invalid input. [Press enter to continue] ")
        return
    a = arr[i]
    clear()
    print("Name: " + a["name"])
    print()
    for i in a["questions"]:
        print("Q: " + i)
        print("A: " + a["questions"][i])
        print()
    input("Press enter to continue: ")

def main():
    while True:
        clear()
        choice = input("Do you want to start (s), view saved answers (v), or exit (e)? > ")
        if choice == "s":
            session()
        elif choice == "v":
            view()
        elif choice == "e":
            exit(0)
        else:
            input("Invalid command. [Press enter to continue]")
    
main()
