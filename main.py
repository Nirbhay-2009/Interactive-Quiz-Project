import tkinter as tk
from questions import questions
from quiz_logic import calculate_score, get_result


# -----------------------------
# Main window
# -----------------------------

window = tk.Tk()
window.title("Interactive Personality Quiz")
window.geometry("600x450")


# -----------------------------
# Variables
# -----------------------------

current_question = 0

selected_answer = tk.IntVar()


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="Interactive Personality Quiz",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Question number
# -----------------------------

question_number_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)

question_number_label.pack()


# -----------------------------
# Question
# -----------------------------

question_label = tk.Label(
    window,
    text="",
    font=("Arial", 15),
    wraplength=500
)

question_label.pack(pady=20)


# -----------------------------
# Radio buttons
# -----------------------------

option_buttons = []

for i in range(4):

    radio = tk.Radiobutton(
        window,
        text="",
        variable=selected_answer,
        value=i,
        font=("Arial", 12)
    )

    radio.pack(anchor="w", padx=100, pady=5)

    option_buttons.append(radio)


# -----------------------------
# Function to show question
# -----------------------------

def show_question():

    question = questions[current_question]

    question_number_label.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    question_label.config(
        text=question["question"]
    )

    for i, letter in enumerate(["A", "B", "C", "D"]):
        option_buttons[i].config(
        text=f"{letter}. {question['options'][letter][0]}"
    )

    selected_answer.set(-1)


# -----------------------------
# Next button function
# -----------------------------

def next_question():

    global current_question

    answer = selected_answer.get()

    if answer == -1:
        return

    # Get the current question
    question = questions[current_question]

    # Get the selected option (A, B, C or D)
    letters = ["A", "B", "C", "D"]
    selected_letter = letters[answer]

    # Find the personality category
    category = question["options"][selected_letter][1]

    # Send the category to quiz_logic.py
    calculate_score(category)

    # Move to the next question
    current_question += 1

    if current_question < len(questions):

        show_question()

    else:

        show_result()


# -----------------------------
# Result function
# -----------------------------

def show_result():

    result = get_result()

    question_number_label.config(
        text="Quiz Completed!"
    )

    question_label.config(
        text=f"Your Personality:\n{result}",
        font=("Arial", 18, "bold")
    )

    for button in option_buttons:
        button.pack_forget()

    next_button.pack_forget()


# -----------------------------
# Next button
# -----------------------------

next_button = tk.Button(
    window,
    text="Next",
    command=next_question,
    font=("Arial", 12),
    width=12
)

next_button.pack(pady=25)


# -----------------------------
# Start with first question
# -----------------------------

show_question()


# -----------------------------
# Run the application
# -----------------------------

window.mainloop()