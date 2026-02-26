import tkinter as tk # imports tkinter for creating the GUI
from tkinter import messagebox # imports messagebox for name input
import csv # to write to csv from main
from quiz_data import load_questions # for loading the questions for the question screen
from quiz_utils import clean_name, character_check, length_check, presence_check, pattern_check # utility functions to clean and validate names
from datetime import datetime # to record a timestamp in the CSV

BG = "#D70032" 
BUTTON_BG = "#F2F2F2"
TEXT = "#FFFFFF"
BUTTON_TEXT = "#111111"

questions = load_questions()

class EconomicQuizApp(tk.Tk):
    
    """
    A class that represents the economic quiz application.

    """

    def __init__(self, questions):
        """"
        Constructs all the necessary attributes for the app and name box.

        Parameters:
        self.name (str): The widget containing the user's name.
        self.questions (list): A list of dictionaries containing 'question' and 'options'.
        self.answer_vars (list): A list of tk.IntVar to store the user's chosen answers.

        """
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
        Builds the question section of the app.

        The function takes the questions from the quiz_data file and populates the screen with the question and the multiple answers available. 
        It asigns a questin number to the question and radio buttons for the answers. It also tracks the user responses

        Parameters:
        self.questions (list): A list of dictionaries containing 'question' and 'options'.
        self.answer_vars (list): A list of tk.IntVar to store the user's chosen answers.

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

        """
        Builds the CSV that the user's responses are written to.

        This function carrys out three actions:
        1. Validation-ensures all questions have been answered.
        2. Score-Counts user selections and work out their score against the correct answers.
        3. Storage-Stores the users name, date, time, score and answers chosen to the quiz_records CSV.

        Parameters:
        self.answers_vars (list): Tracks the answers chosen.
        self.questions (list): Recalls on the CSV that contains the correct answers.
        self.name_entry (tk.Entry): The widget containing the user's name.

        Returns:
        Returns an error message if questions are not answered.
        Writes a new row to the quiz_records CSV.
        Switches the first screen to the Thank You screen.

        """
        
        skipped_questions = [i + 1 for i, var in enumerate(self.answer_vars) if var.get() == -1] 
        if skipped_questions:
            missing_str = ", ".join(map(str, skipped_questions))
            messagebox.showwarning(
                "Incomplete Quiz", 
                f"Please answer all questions before submitting. Missing questions: {missing_str}"
            )
            return # this brings up an error message if all questions are not answered
        
        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.validate_name_with_messages(st_name):
            self.score = 0
            for i, var in enumerate(self.answer_vars):
                user_choice = var.get()
                correct_choice = self.questions[i]["correct"]

                if user_choice == correct_choice:
                    self.score += 1 # counts the score for quiz

            answers = []
            for var in self.answer_vars:
                answers.append(var.get())
                    
            with open("quiz_records.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([st_name, timestamp, self.score, answers])
                print("Data successfully written to CSV.") # writes to csv and prints this message when successfully written

            self.build_thank_you_screen(st_name)
            
            
    def build_thank_you_screen(self, name):
        
        """
        Shows the final screen.
        
        This function builds the Thank You screen where the user is thanked for submitting their answers,
        their score is displayed and they are praised for their hard work. 
        This screen also displays a quit button and the company logo.
        
        Parameters:
        self.score (int): Counts the number of correct answers chosen.
        self.questions (list): Recalls on the CSV that contains the correct answers.
        self.logo (tk.PhotoImage): Recalls on the Logo png file and displays on the thank you screen.

        Returns:
        "Thank you for submitting your answers, {name}!".
        "{name}, your score is: {self.score}/{len(self.questions)}".
        "Well done, keep up the hard work!"
        Displays the quit button.
        Displays the logo image below.

        """

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
            text=f"{name}, your score is: {self.score}/{len(self.questions)}", # produces users score for quiz
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
        
        self.logo_image = tk.PhotoImage(file="Logo.png") # adds company logo to thank you screen
        self.logo_image = self.logo_image.zoom(2,2)
        self.logo_image = self.logo_image.subsample(2,2)
        self.logo_label = tk.Label(self, image=self.logo_image, bg=BG)
        self.logo_label.pack(pady=20)
        
    def validate_name_with_messages(self, cleaned_name: str) -> bool:
        
        """
        Validates the cleaned name and shows an error message if invalid.

        This function cleans the name using and shows an error message if the name does not adhere to the 4 rules:
        1.Presence check-ensures the name is not blank.
        2.Length check-ensures the name is between 2 and 50 characters.
        3.Character check-ensures the name does not contain any numbers.
        4.Pattern check-ensures the name does not contain any invalid punctuation.

        Parameters:
        cleaned_name (str): The name after the white spaces has been removed and the name has been correctly capitalised.

        Returns:
        bool: The function returns true if the name is valid, False if the name is invalid. 
        This is not a pure function because it depends on the message box.

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
        
        """
        Removes all widgets from the window.
        
        This fucntions removes all widgets from the screen so the user knows they are done with the quiz.
        
        """
        
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = EconomicQuizApp(questions)
    app.mainloop()
