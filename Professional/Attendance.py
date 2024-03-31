import random
import datetime
import tkinter as tk
from tkinter import messagebox,simpledialog

now = datetime.datetime.now()
today = now.date()

questions = {
    "1. Simple Interest on Rs 1000 after 1 year at 10% is? ": "1100",
    "2. Java is: Function based or Object Oriented?": "object oriented",
    "3. The Rashidun Caliphate lasted for how many years?": "30",
    "4. When was the 18th Amendment made in the Pak Constitution?": "2010"
}

class AttendanceSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Attendance System")

        self.label = tk.Label(master, text="Select an option:")
        self.label.pack()

        self.mark_button = tk.Button(master, text="Mark Attendance", command=self.mark_attendance)
        self.mark_button.pack()

        self.view_button = tk.Button(master, text="View Attendance", command=self.view_attendance)
        self.view_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

    def ask_question(self):
        question = random.choice(list(questions.keys()))
        answer = simpledialog.askstring("Input", question)
        return answer.lower() == questions[question].lower()

    def mark_attendance(self):
        subject = simpledialog.askstring("Input", "Enter Subject:")
        status = simpledialog.askstring("Input", "Is this the first attendance of the day? (y/n)")
        file_mode = 'w' if status.lower() == "y" else 'a'

        name = simpledialog.askstring("Input", "Enter student's name:")
        roll = simpledialog.askstring("Input", "Roll No:")

        messagebox.showinfo("Info", "You must answer this question to mark your presence. Get it wrong and you are absent.")

        if self.ask_question():
            with open(f"{subject} Attendance {today}.txt", file_mode) as f:
                f.write(f"\n{name}:{roll}")
        else:
            messagebox.showinfo("Info", f"Incorrect. The correct answer is {questions}.\nYou have been marked as absent for date {today}")

    def view_attendance(self):
        subject = simpledialog.askstring("Input", """Enter subject to view Attendance.
            1. Pakistan Studies
            2. OOPs
            3. Islamiat
            4. Technical Writing
            5. Electronics""")

        date = simpledialog.askstring("Input", "Write required date in numbers (format yyyy-mm-dd)")

        try:
            with open(f"{subject} Attendance {date}.txt") as f:
                content = f.read()
                messagebox.showinfo("Attendance", content)
        except FileNotFoundError:
            messagebox.showinfo("Info", "Attendance file not found for the specified subject and date.")
        except Exception as e:
            messagebox.showinfo("Info", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSystemGUI(root)
    root.mainloop()
