import random
import datetime

now = datetime.datetime.now()
today = now.date()

questions={
    "1. Simple Interest on Rs 1000 after 1 year at 10% is? "       :"1100",
    "2. Java is: Function based or Object Oriented?"               :"object oriented",
    "3. The Rashidun Caliphate lasted for how many years?"         :"30",
    "4. When was the 18th Amendment made in the Pak Constitution?": "2010"
}

def mark_attendance():
    
    subject=input(">> Subject:")
    status=input("Is this the first attendance of the day?(y/n)")
    if status.lower()=="y":
        file_mode='w'
    else:
        file_mode='a'
        
    name=input("Enter student's name: ")
    roll=input("Roll No:")
    
    print("You must answer this question to mark your presence. Get it wrong and you are absent.")
    
    question = random.choice(list(questions.keys()))

    answer = input(question + " ").lower()

    if answer.lower() == questions[question].lower(): 
        with open(f"{subject} Attendance {today}.txt", file_mode) as f:
            f.write(f"\n{name}:{roll}")
    else:
        print("Incorrect. The correct answer is", questions[question])
        print(f"You have been marked as absent for date {today}")
        
        
def view_attendance():
    sub=input("""Enter subject to view Attendance.
            1. Pakistan Studies
            2. OOPs
            3. Islamiat
            4. Technical Writing
            5. Electronics\n""")
    
    date=input("Write required date in numbers (format yyyy-mm-dd)")
    try:
        with open(f"{sub} Attendance {date}.txt") as f:
            content = f.read()
        print(content)
        
    except FileNotFoundError:
        print("Attendance file not found for the specified subject and date.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    function=input("""Instructions...
        1. Mark Attendance
        2. View Attendance
        3. Exit\n""")

    if function == "1":
        mark_attendance()

    elif function == "2":
        view_attendance()

    elif function=="3":
        break