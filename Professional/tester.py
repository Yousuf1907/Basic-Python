import random
import datetime

now = datetime.datetime.now()
today = now.date()
print("Today's date:", today)  # Output: 2024-01-17 (format: YYYY-MM-DD)

questions = {
   "1. Simple Interest on Rs 1000 after 1 year at 10% is? ": "1100",
   "2. Who is the current ODI Captain for Pak": "shaheen afridi"
}

question = random.choice(list(questions.keys()))

answer = input(question + " ").lower()

if answer.lower() == questions[question].lower(): 
   print("Correct!")
else:
   print("Incorrect. The correct answer is", questions[question])
