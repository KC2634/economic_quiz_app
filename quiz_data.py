import csv # for reading the CSV file

def load_questions(filepath="questions.csv"):
    
    """
    Load questions from questions CSV file and return a list of question dictionaries.

    This functions loads the questions from the 'questions' CSV file and turns them into a list of question dictionaries.
    The output depends on the contents of questions.csv, therefore it is not pure.
    If the file changes, the function returns different results for the same input.

    Parameters:
    filepath (str): The path to the questions CSV file.

    Returns:
    list: 
    -'question' (str): The text of the question.
    -'options' (list): A list of options A to D.
    -'correct' (int): The index of the correct answer (0-3).

    """
    
    questions = []

    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append({
                "question": row["question"],
                "options": [
                    row["option_a"],
                    row["option_b"],
                    row["option_c"],
                    row["option_d"],
                ],
                "correct": int(row["correct"])
            })

    return questions

