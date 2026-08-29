import tkinter as tk
from tkinter import ttk

from questions import questions
from quiz_logic import calculate_score, get_result, scores


# =====================================================
# MAIN WINDOW
# =====================================================

window = tk.Tk()

window.title("Interactive Personality & Career Quiz")

# Bigger window so everything fits properly
window.geometry("900x650")

window.resizable(False, False)

window.configure(bg="#EEF3FF")


# =====================================================
# COLORS
# =====================================================

PURPLE = "#402080"
LIGHT_PURPLE = "#5B2CB6"

BLUE = "#2563EB"
GREEN = "#22A85A"

WHITE = "#FFFFFF"

BACKGROUND = "#EEF3FF"

TEXT = "#202124"

BORDER = "#D8DCE8"


# =====================================================
# VARIABLES
# =====================================================

current_question = 0

selected_answer = tk.IntVar(value=-1)


# =====================================================
# HEADER
# =====================================================

header = tk.Frame(
    window,
    bg=PURPLE,
    height=115
)

header.pack(fill="x")

header.pack_propagate(False)


# Brain icon

brain_label = tk.Label(
    header,
    text="🧠",
    font=("Segoe UI Emoji", 38),
    bg=PURPLE,
    fg=WHITE
)

brain_label.pack(
    side="left",
    padx=(35, 15)
)


# Header text

header_text = tk.Frame(
    header,
    bg=PURPLE
)

header_text.pack(
    side="left",
    pady=18
)


title_label = tk.Label(
    header_text,
    text="Interactive Personality & Career Quiz",
    font=("Arial", 23, "bold"),
    bg=PURPLE,
    fg=WHITE
)

title_label.pack(anchor="w")


subtitle_label = tk.Label(
    header_text,
    text="Answer honestly to discover the best career paths for you!",
    font=("Arial", 11),
    bg=PURPLE,
    fg=WHITE
)

subtitle_label.pack(
    anchor="w",
    pady=(5, 0)
)


# =====================================================
# MAIN FRAME
# =====================================================

main_frame = tk.Frame(
    window,
    bg=BACKGROUND
)

main_frame.pack(
    fill="both",
    expand=True
)


# =====================================================
# PROGRESS FRAME
# =====================================================

progress_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

progress_frame.pack(
    fill="x",
    padx=30,
    pady=(18, 12)
)


question_number_label = tk.Label(
    progress_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=TEXT
)

question_number_label.pack(
    side="left",
    padx=15,
    pady=12
)


# Progress bar

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Quiz.Horizontal.TProgressbar",
    troughcolor="#DDE1EA",
    background=BLUE,
    thickness=13
)


progress_bar = ttk.Progressbar(
    progress_frame,
    style="Quiz.Horizontal.TProgressbar",
    orient="horizontal",
    length=430,
    mode="determinate"
)

progress_bar.pack(
    side="left",
    padx=10
)


percentage_label = tk.Label(
    progress_frame,
    text="",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=TEXT
)

percentage_label.pack(
    side="left",
    padx=10
)


# =====================================================
# QUESTION CARD
# =====================================================

question_card = tk.Frame(
    main_frame,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

question_card.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 18)
)


# Question number

number_label = tk.Label(
    question_card,
    text="1",
    font=("Arial", 16, "bold"),
    bg=LIGHT_PURPLE,
    fg=WHITE,
    width=3,
    pady=3
)

number_label.pack(
    anchor="w",
    padx=22,
    pady=(15, 7)
)


# Question

question_label = tk.Label(
    question_card,
    text="",
    font=("Arial", 16, "bold"),
    bg=WHITE,
    fg=TEXT,
    wraplength=780,
    justify="left"
)

question_label.pack(
    anchor="w",
    padx=22,
    pady=(0, 12)
)


# =====================================================
# ANSWER OPTIONS
# =====================================================

option_buttons = []


for i in range(4):

    radio = tk.Radiobutton(
        question_card,

        text="",

        variable=selected_answer,

        value=i,

        font=("Arial", 12),

        bg=WHITE,

        fg=TEXT,

        activebackground="#F1F4FF",

        activeforeground=TEXT,

        selectcolor="#E5EBFF",

        anchor="w",

        padx=12,

        pady=7,

        relief="solid",

        bd=1,

        highlightthickness=0,

        wraplength=750
    )

    radio.pack(
        fill="x",
        padx=22,
        pady=3
    )

    option_buttons.append(radio)


# =====================================================
# NEXT BUTTON
# =====================================================

next_button = tk.Button(
    question_card,

    text="Next  →",

    command=lambda: next_question(),

    font=("Arial", 12, "bold"),

    bg=BLUE,

    fg=WHITE,

    activebackground=LIGHT_PURPLE,

    activeforeground=WHITE,

    relief="flat",

    padx=25,

    pady=8,

    cursor="hand2"
)

next_button.pack(
    anchor="e",

    padx=22,

    pady=(8, 12)
)


# =====================================================
# SHOW QUESTION
# =====================================================

def show_question():

    question = questions[current_question]

    total_questions = len(questions)

    number = current_question + 1


    # -----------------------------------------------
    # Question number
    # -----------------------------------------------

    question_number_label.config(
        text=f"Question {number} of {total_questions}"
    )


    # -----------------------------------------------
    # Progress
    # -----------------------------------------------

    percentage = int(
        (number / total_questions) * 100
    )

    progress_bar["value"] = percentage

    percentage_label.config(
        text=f"{percentage}% Complete"
    )


    # -----------------------------------------------
    # Question number box
    # -----------------------------------------------

    number_label.config(
        text=str(number)
    )


    # -----------------------------------------------
    # Question text
    # -----------------------------------------------

    question_label.config(
        text=question["question"]
    )


    # -----------------------------------------------
    # Options
    # -----------------------------------------------

    letters = ["A", "B", "C", "D"]


    for i in range(4):

        letter = letters[i]

        option_text = question["options"][letter][0]

        option_buttons[i].config(
            text=f"{letter}.   {option_text}"
        )


    # -----------------------------------------------
    # Clear previous selection
    # -----------------------------------------------

    selected_answer.set(-1)


    # -----------------------------------------------
    # Change button on last question
    # -----------------------------------------------

    if number == total_questions:

        next_button.config(
            text="Finish  ✓",
            bg=GREEN,
            activebackground="#16803C"
        )

    else:

        next_button.config(
            text="Next  →",
            bg=BLUE,
            activebackground=LIGHT_PURPLE
        )


# =====================================================
# NEXT QUESTION
# =====================================================

def next_question():

    global current_question


    # Check whether an answer was selected

    answer = selected_answer.get()


    if answer == -1:

        # No answer selected
        return


    # -----------------------------------------------
    # Get current question
    # -----------------------------------------------

    question = questions[current_question]


    # -----------------------------------------------
    # Convert number into A/B/C/D
    # -----------------------------------------------

    letters = ["A", "B", "C", "D"]

    selected_letter = letters[answer]


    # -----------------------------------------------
    # Get personality category
    # -----------------------------------------------

    category = question["options"][selected_letter][1]


    # -----------------------------------------------
    # Calculate score
    # -----------------------------------------------

    calculate_score(category)


    # -----------------------------------------------
    # Move to next question
    # -----------------------------------------------

    current_question += 1


    # -----------------------------------------------
    # Check if questions are remaining
    # -----------------------------------------------

    if current_question < len(questions):

        show_question()

    else:

        show_result()


# =====================================================
# RESULT INFORMATION
# =====================================================

result_information = {

    "Analytical Thinker": {

        "description":
        "You love logic, enjoy solving problems, "
        "and think things through step by step. "
        "You are detail-oriented and analytical.",

        "careers":
        "• Data Analyst\n"
        "• Software Developer\n"
        "• Research Scientist"
    },


    "Creative Innovator": {

        "description":
        "You enjoy creating new ideas and thinking "
        "of unique solutions. You like creativity "
        "and exploring new possibilities.",

        "careers":
        "• UI/UX Designer\n"
        "• Content Creator\n"
        "• Creative Director"
    },


    "Leader": {

        "description":
        "You naturally take responsibility and enjoy "
        "organizing people and activities. You are "
        "confident and goal-oriented.",

        "careers":
        "• Project Manager\n"
        "• Business Manager\n"
        "• Entrepreneur"
    },


    "Social Helper": {

        "description":
        "You enjoy helping people and working together. "
        "You are supportive, friendly and a good communicator.",

        "careers":
        "• Teacher\n"
        "• HR Manager\n"
        "• Counselor"
    }
}


# =====================================================
# SHOW RESULT
# =====================================================

def show_result():

    result = get_result()


    # -----------------------------------------------
    # Hide question screen
    # -----------------------------------------------

    progress_frame.pack_forget()

    question_card.pack_forget()


    # -----------------------------------------------
    # Create result screen
    # -----------------------------------------------

    result_frame = tk.Frame(
        main_frame,
        bg=BACKGROUND
    )

    result_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=18
    )


    # -----------------------------------------------
    # Trophy
    # -----------------------------------------------

    trophy = tk.Label(
        result_frame,
        text="🏆",
        font=("Segoe UI Emoji", 34),
        bg=BACKGROUND
    )

    trophy.pack()


    # -----------------------------------------------
    # Completed
    # -----------------------------------------------

    completed = tk.Label(
        result_frame,
        text="Quiz Completed!",
        font=("Arial", 23, "bold"),
        bg=BACKGROUND,
        fg="#16803C"
    )

    completed.pack()


    # -----------------------------------------------
    # Personality heading
    # -----------------------------------------------

    heading = tk.Label(
        result_frame,
        text="Your Personality Type is:",
        font=("Arial", 11, "bold"),
        bg=BACKGROUND,
        fg=TEXT
    )

    heading.pack(
        pady=(3, 4)
    )


    # -----------------------------------------------
    # Personality result
    # -----------------------------------------------

    result_box = tk.Label(
        result_frame,
        text=f"🧠  {result}",
        font=("Arial", 17, "bold"),
        bg=GREEN,
        fg=WHITE,
        padx=25,
        pady=8
    )

    result_box.pack(
        pady=(0, 12)
    )


    # =================================================
    # INFORMATION CARDS
    # =================================================

    cards_frame = tk.Frame(
        result_frame,
        bg=BACKGROUND
    )

    cards_frame.pack(
        fill="x",
        pady=5
    )


    # -----------------------------------------------
    # ABOUT YOU CARD
    # -----------------------------------------------

    about_card = tk.Frame(
        cards_frame,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    about_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 8)
    )


    about_title = tk.Label(
        about_card,
        text="👤  About You",
        font=("Arial", 14, "bold"),
        bg=WHITE,
        fg=TEXT
    )

    about_title.pack(
        anchor="w",
        padx=18,
        pady=(15, 7)
    )


    about_text = tk.Label(
        about_card,
        text=result_information[result]["description"],
        font=("Arial", 10),
        bg=WHITE,
        fg=TEXT,
        wraplength=350,
        justify="left"
    )

    about_text.pack(
        anchor="w",
        padx=18,
        pady=(0, 15)
    )


    # -----------------------------------------------
    # CAREER CARD
    # -----------------------------------------------

    career_card = tk.Frame(
        cards_frame,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    career_card.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(8, 0)
    )


    career_title = tk.Label(
        career_card,
        text="💼  Career Suggestions",
        font=("Arial", 14, "bold"),
        bg=WHITE,
        fg=TEXT
    )

    career_title.pack(
        anchor="w",
        padx=18,
        pady=(15, 7)
    )


    career_text = tk.Label(
        career_card,
        text=result_information[result]["careers"],
        font=("Arial", 10),
        bg=WHITE,
        fg=TEXT,
        justify="left"
    )

    career_text.pack(
        anchor="w",
        padx=18,
        pady=(0, 15)
    )


    # =================================================
    # RESTART BUTTON
    # =================================================

    restart_button = tk.Button(
        result_frame,

        text="↻  Restart Quiz",

        command=lambda: restart_quiz(result_frame),

        font=("Arial", 12, "bold"),

        bg=GREEN,

        fg=WHITE,

        activebackground="#16803C",

        activeforeground=WHITE,

        relief="flat",

        padx=25,

        pady=8,

        cursor="hand2"
    )

    restart_button.pack(
        pady=12
    )


# =====================================================
# RESTART QUIZ
# =====================================================

def restart_quiz(result_frame):

    global current_question


    # Reset scores

    for category in scores:

        scores[category] = 0


    # Go back to question 1

    current_question = 0


    # Remove result screen

    result_frame.destroy()


    # Show question interface

    progress_frame.pack(
        fill="x",
        padx=30,
        pady=(18, 12)
    )


    question_card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 18)
    )


    show_question()


# =====================================================
# START QUIZ
# =====================================================

show_question()


# =====================================================
# RUN PROGRAM
# =====================================================

window.mainloop()