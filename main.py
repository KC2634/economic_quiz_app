import tkinter as tk
import csv
from quiz_data import load_questions

BG = "#ffe1a5"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"

questions = load_questions()

class EconomicQuiz(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("History Quiz")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.configure(bg=BG)
        self.geometry("600x700")
        self.name = tk.StringVar()
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []

if __name__== "__main__":
    app = EconomicQuiz(questions)
    app.mainloop()
