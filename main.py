import tkinter as tk # for creating the GUI
from tkinter import messagebox
import csv # to write to csv from main
from quiz_data import load_questions # for loading the questions
# utility functions to clean and validate names 👇
from quiz_utils import clean_name, character_check, length_check, presence_check, pattern_check
from datetime import datetime # to record a timestamp

BG = "#D70032"
BUTTON_BG = "#F2F2F2"
TEXT = "#FFFFFF"
BUTTON_TEXT = "#111111"

questions = load_questions()

class EconomicQuizApp(tk.Tk):
    
    """
    A class that represents the quiz application.
    """

    def __init__(self, questions):
        super().__init__()
        self.title("Economic Quiz")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.configure(bg=BG)
        self.geometry("700x2000")
        self.name = tk.StringVar()
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []


        self.name_label = tk.Label(
            self,
            text="Please enter your name in the box below 😊",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 18, "bold")
        )
        self.name_label.pack(pady=15)

        self.name_entry = tk.Entry(
            self,
            textvariable=self.name,
            font=("Segoe UI", 18),
            fg=BUTTON_TEXT
        )
        self.name_entry.pack(pady=15)

        self.build_question_screen()

        self.submit_button = tk.Button(
            self,
            text="SUBMIT!",
            font=("Segoe UI", 16),
            fg=BUTTON_TEXT,
            bg=BUTTON_BG,
            command=self.handle_submit
        )
        self.submit_button.pack(pady=15)

    def build_question_screen(self):
        
        """
        Builds the question section.
        """

        question_number = 1

        for question in self.questions:
            q_label = tk.Label(
                self,
                text=f"Question {question_number}. {question['question']}",
                font=("Segoe UI", 18),
                wraplength=700,  # wrap the text if it's too long
                justify="center",
                fg = TEXT,  
                bg = BG
            )
            q_label.pack(anchor="w", padx=40, pady=(20, 5))

            answer_var = tk.IntVar(value=-1)
            self.answer_vars.append(answer_var)

            option_value = 0
            for option in question["options"]:
                rb = tk.Radiobutton(
                    self,
                    text=option,
                    variable=answer_var,
                    value=option_value,
                    font=("Segoe UI", 14),
                    fg = TEXT,
                    bg=BG
                )
                rb.pack(anchor="w", padx=60)
                option_value += 1

            question_number += 1
    
    def handle_submit(self):
        
        skipped_questions = [i + 1 for i, var in enumerate(self.answer_vars) if var.get() == -1]
        if skipped_questions:
            missing_str = ", ".join(map(str, skipped_questions))
            messagebox.showwarning(
                "Incomplete Quiz", 
                f"Please answer all questions before submitting. Missing questions: {missing_str}"
            )
            return


        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.validate_name_with_messages(st_name):
            self.score = 0
            for i, var in enumerate(self.answer_vars):
                user_choice = var.get()
                correct_choice = self.questions[i]["correct"]

                if user_choice == correct_choice:
                    self.score += 1

            answers = []
            for var in self.answer_vars:
                answers.append(var.get())
                    
            with open("quiz_records.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([st_name, timestamp, self.score, answers])
                print("Data successfully written to CSV.")

            self.build_thank_you_screen(st_name)
            
            
    def build_thank_you_screen(self, name):
        
        """Shows the final confirmation screen."""

        self.clear_screen()

        tk.Label(
            self,
            text=f"Thank you for submitting your answers, {name}!",
            font=("Segoe UI", 18),
            fg = TEXT,
            bg = BG
        ).pack(pady=20)

        tk.Label(
            self,
            text=f"{name}, your score is: {self.score}/{len(self.questions)}",
            font=("Segoe UI", 24),
            wraplength=500,
            justify="center",
            fg = TEXT,
            bg = BG
        ).pack(pady=10)

        tk.Label(
            self,
            text="Well done, keep up the hard work!",
            font=("Segoe UI", 18),
            wraplength=500,
            justify="center",
            fg = TEXT,
            bg = BG
        ).pack(pady=20)

        tk.Button(
            self,
            font=("Segoe UI", 18),
            fg=BUTTON_TEXT,
            bg="#F2F2F2",
            text="QUIT",
            command=self.destroy
        ).pack(pady=30)
        
        self.logo_image = tk.PhotoImage(file="Logo.png")
        self.logo_image = self.logo_image.zoom(2,2)
        self.logo_image = self.logo_image.subsample(2,2)
        self.logo_label = tk.Label(self, image=self.logo_image, bg=BG)
        self.logo_label.pack(pady=20)
        
    def validate_name_with_messages(self, cleaned_name: str) -> bool:
        
        """
        Validates the cleaned name and shows an error message if invalid.
        Returns True if the name is valid. Not pure because depends on messagebox.
        """
        valid = True

        if not presence_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Please enter your name."
            )
            valid = False

        if valid and not length_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Name must be between 2 and 50 characters."
            )
            valid = False

        if valid and not character_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Names must only contain letters, spaces, or hyphens."
            )
            valid = False

        if valid and not pattern_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Names must only contain letter, spaces or hyphens."
            )
            valid = False

        return valid

    def clear_screen(self):
        
        """Removes all widgets from the window."""
        
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = EconomicQuizApp(questions)
    app.mainloop()
