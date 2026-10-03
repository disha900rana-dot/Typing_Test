# import time 
# import random

# sentences = [
#     "The quick brown fox jumps over the lazy dog.",
#     "A journey of a thousand miles begins with a single step.",
#     "This is the way for us to reference the object of the class."
# ]

# def measure_accuracy(user_input, test_sentence):
#     correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
#     accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
#     return accuracy

# def typing_test():
#     test_sentence = random.choice(sentences)
#     print("Type the following sentence as fast as you can:")
#     print(test_sentence)
#     input("Press Enter when you are ready...")
#     start_time = time.time()
#     user_input = input("\nStart typing:\n")
#     end_time = time.time()
#     time_taken = end_time - start_time 
#     word_count = len(test_sentence.split(" "))

#     print("Results:")
#     print(f"Time taken: {time_taken} seconds")
#     print(f"Words typed: {word_count}")
#     print(f"Typing speed: {word_count / (time_taken / 60):.2f} words per minute")
#     accuracy = measure_accuracy(user_input, test_sentence)
#     print(f"Accuracy: {accuracy:.2f}%")

# typing_test()

import tkinter as tk
import random
import time


# =========================================================
# SENTENCES
# =========================================================

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class.",
    "Practice makes a person perfect and improves typing speed.",
    "Learning Python is fun when you practice every day."
]


# =========================================================
# COLORS
# =========================================================

PINK = "#F8BBD0"
LIGHT_PINK = "#FFF5F9"
DARK_PINK = "#D81B60"

BLUE = "#B3E5FC"
LIGHT_BLUE = "#E1F5FE"
DARK_BLUE = "#0288D1"

YELLOW = "#FFF59D"
DARK_YELLOW = "#F9A825"

WHITE = "#FFFFFF"
TEXT = "#5D4057"


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("🎀 Typing Speed Test 🎀")

root.geometry("1000x750")

root.configure(bg=LIGHT_PINK)

root.resizable(False, False)


# =========================================================
# VARIABLES
# =========================================================

current_sentence = ""

start_time = None

test_started = False

test_finished = False


# =========================================================
# ACCURACY FUNCTION
# =========================================================

def measure_accuracy(user_input, test_sentence):

    if not test_sentence:
        return 0

    correct_chars = sum(
        1
        for a, b in zip(user_input, test_sentence)
        if a == b
    )

    accuracy = (
        correct_chars / len(test_sentence)
    ) * 100

    return accuracy


# =========================================================
# START TEST
# =========================================================

def start_test():

    global current_sentence
    global start_time
    global test_started
    global test_finished

    # Choose a random sentence
    current_sentence = random.choice(sentences)

    # Reset variables
    start_time = None
    test_started = False
    test_finished = False

    # Display sentence
    sentence_label.config(
        text=current_sentence
    )

    # Clear typing box
    typing_box.config(
        state="normal"
    )

    typing_box.delete(
        "1.0",
        tk.END
    )

    # Reset results
    time_value.config(text="--")
    words_value.config(text="--")
    speed_value.config(text="--")
    accuracy_value.config(text="--")

    # Reset status
    status_label.config(
        text="Start typing when you are ready! 💕",
        fg=DARK_BLUE
    )

    # Enable typing
    typing_box.focus()

    # Disable start button
    start_button.config(
        state="disabled",
        text="Typing... 💕"
    )


# =========================================================
# CHECK TYPING
# =========================================================

def check_typing(event=None):

    global start_time
    global test_started

    # No sentence selected
    if not current_sentence:
        return

    # Test already finished
    if test_finished:
        return

    # Get text from typing box
    user_input = typing_box.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    # Start timer with first character
    if not test_started and len(user_input) > 0:

        start_time = time.time()

        test_started = True

        status_label.config(
            text="Keep typing... You are doing great! ✨",
            fg=DARK_PINK
        )

    # Check if sentence is completed
    if len(user_input) >= len(current_sentence):

        finish_test()


# =========================================================
# FINISH TEST
# =========================================================

def finish_test():

    global test_started
    global test_finished

    if not test_started:
        return

    # Get final input
    user_input = typing_box.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    # Stop timer
    end_time = time.time()

    # Calculate total time
    time_taken = end_time - start_time

    if time_taken <= 0:
        time_taken = 0.01

    # =====================================================
    # WORD COUNT
    # =====================================================

    word_count = len(
        user_input.split()
    )

    # =====================================================
    # WORDS PER MINUTE
    # =====================================================

    # Convert seconds into minutes
    minutes = time_taken / 60

    # Calculate typing speed
    words_per_minute = word_count / minutes

    # =====================================================
    # ACCURACY
    # =====================================================

    accuracy = measure_accuracy(
        user_input,
        current_sentence
    )

    # =====================================================
    # DISPLAY TIME
    # =====================================================

    time_value.config(
        text=f"{time_taken:.2f} sec"
    )

    # =====================================================
    # DISPLAY WORDS
    # =====================================================

    words_value.config(
        text=str(word_count)
    )

    # =====================================================
    # DISPLAY WPM
    # =====================================================

    speed_value.config(
        text=f"{words_per_minute:.2f} WPM"
    )

    # =====================================================
    # DISPLAY ACCURACY
    # =====================================================

    accuracy_value.config(
        text=f"{accuracy:.2f}%"
    )

    # =====================================================
    # SHOW RESULT MESSAGE
    # =====================================================

    status_label.config(
        text=(
            f"🎉 Test Complete!   "
            f"Speed: {words_per_minute:.2f} WPM   "
            f"Accuracy: {accuracy:.2f}%"
        ),
        fg=DARK_PINK
    )

    # =====================================================
    # FINISH TEST
    # =====================================================

    test_started = False

    test_finished = True

    # Disable typing box
    typing_box.config(
        state="disabled"
    )

    # Enable start button
    start_button.config(
        state="normal",
        text="Start Again 🎀"
    )


# =========================================================
# RESET TEST
# =========================================================

def reset_test():

    global current_sentence
    global start_time
    global test_started
    global test_finished

    current_sentence = ""

    start_time = None

    test_started = False

    test_finished = False

    # Reset sentence
    sentence_label.config(
        text="Click 'Start Test' to get your sentence ✨"
    )

    # Clear typing box
    typing_box.config(
        state="normal"
    )

    typing_box.delete(
        "1.0",
        tk.END
    )

    # Reset results
    time_value.config(text="--")
    words_value.config(text="--")
    speed_value.config(text="--")
    accuracy_value.config(text="--")

    # Reset status
    status_label.config(
        text="Ready for another test? 🌸",
        fg=DARK_BLUE
    )

    # Enable start button
    start_button.config(
        state="normal",
        text="Start Test 🎀"
    )


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg=PINK,
    height=115
)

header.pack(
    fill="x",
    padx=25,
    pady=(20, 10)
)


title = tk.Label(
    header,
    text="♥  Typing Speed Test  ♥",
    font=("Segoe Script", 32, "bold"),
    bg=PINK,
    fg=DARK_PINK
)

title.pack(
    pady=(15, 0)
)


subtitle = tk.Label(
    header,
    text="Type  •  Improve  •  Be Faster ✨",
    font=("Segoe Script", 15),
    bg=PINK,
    fg=TEXT
)

subtitle.pack()


# =========================================================
# MAIN TEST FRAME
# =========================================================

test_frame = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=DARK_PINK,
    highlightthickness=2
)

test_frame.pack(
    fill="x",
    padx=50,
    pady=10
)


# =========================================================
# INSTRUCTION
# =========================================================

instruction = tk.Label(
    test_frame,
    text="Type the following sentence as fast as you can:",
    font=("Segoe Script", 18, "bold"),
    bg=YELLOW,
    fg=TEXT,
    padx=20,
    pady=10
)

instruction.pack(
    pady=(20, 15)
)


# =========================================================
# SENTENCE
# =========================================================

sentence_label = tk.Label(
    test_frame,
    text="Click 'Start Test' to get your sentence ✨",
    font=("Segoe Script", 18),
    bg=LIGHT_BLUE,
    fg=DARK_BLUE,
    wraplength=820,
    padx=25,
    pady=20
)

sentence_label.pack(
    fill="x",
    padx=35
)


# =========================================================
# STATUS
# =========================================================

status_label = tk.Label(
    test_frame,
    text="Ready? Click Start Test! 💕",
    font=("Segoe Script", 14, "bold"),
    bg=WHITE,
    fg=DARK_BLUE
)

status_label.pack(
    pady=(15, 5)
)


# =========================================================
# TYPING BOX
# =========================================================

typing_box = tk.Text(
    test_frame,
    height=4,
    font=("Segoe Script", 16),
    bg=LIGHT_PINK,
    fg=TEXT,
    insertbackground=DARK_PINK,
    wrap="word",
    relief="flat",
    padx=15,
    pady=15
)

typing_box.pack(
    fill="x",
    padx=35,
    pady=15
)


# Check typing after every key
typing_box.bind(
    "<KeyRelease>",
    check_typing
)


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(
    test_frame,
    bg=WHITE
)

button_frame.pack(
    pady=(0, 25)
)


# =========================================================
# START BUTTON
# =========================================================

start_button = tk.Button(
    button_frame,
    text="Start Test 🎀",
    command=start_test,
    font=("Segoe Script", 16, "bold"),
    bg=DARK_PINK,
    fg=WHITE,
    activebackground="#AD1457",
    activeforeground=WHITE,
    relief="flat",
    padx=35,
    pady=10,
    cursor="hand2"
)

start_button.pack(
    side="left",
    padx=10
)


# =========================================================
# RESET BUTTON
# =========================================================

reset_button = tk.Button(
    button_frame,
    text="Reset ↻",
    command=reset_test,
    font=("Segoe Script", 16, "bold"),
    bg=DARK_YELLOW,
    fg=TEXT,
    activebackground="#FBC02D",
    activeforeground=TEXT,
    relief="flat",
    padx=35,
    pady=10,
    cursor="hand2"
)

reset_button.pack(
    side="left",
    padx=10
)


# =========================================================
# RESULTS TITLE
# =========================================================

results_title = tk.Label(
    root,
    text="♥  Your Results  ♥",
    font=("Segoe Script", 22, "bold"),
    bg=LIGHT_PINK,
    fg=DARK_PINK
)

results_title.pack(
    pady=(15, 5)
)


# =========================================================
# RESULTS FRAME
# =========================================================

results_frame = tk.Frame(
    root,
    bg=LIGHT_PINK
)

results_frame.pack(
    padx=45,
    pady=5
)


# =========================================================
# RESULT CARD FUNCTION
# =========================================================

def create_result_card(
    parent,
    title,
    value,
    color,
    icon
):

    card = tk.Frame(
        parent,
        bg=color,
        width=205,
        height=135,
        highlightbackground=WHITE,
        highlightthickness=2
    )

    card.pack(
        side="left",
        padx=8
    )

    card.pack_propagate(False)

    # Icon
    icon_label = tk.Label(
        card,
        text=icon,
        font=("Segoe UI Symbol", 25),
        bg=color,
        fg=DARK_PINK
    )

    icon_label.pack(
        pady=(8, 0)
    )

    # Title
    title_label = tk.Label(
        card,
        text=title,
        font=("Segoe Script", 13, "bold"),
        bg=color,
        fg=TEXT
    )

    title_label.pack()

    # Value
    value_label = tk.Label(
        card,
        text=value,
        font=("Segoe Script", 17, "bold"),
        bg=WHITE,
        fg=DARK_PINK,
        width=14
    )

    value_label.pack(
        pady=8
    )

    return value_label


# =========================================================
# RESULT CARDS
# =========================================================

time_value = create_result_card(
    results_frame,
    "Time Taken",
    "--",
    PINK,
    "⏱"
)


words_value = create_result_card(
    results_frame,
    "Words Typed",
    "--",
    BLUE,
    "▤"
)


speed_value = create_result_card(
    results_frame,
    "Speed / Minute",
    "--",
    YELLOW,
    "⚡"
)


accuracy_value = create_result_card(
    results_frame,
    "Accuracy",
    "--",
    PINK,
    "◎"
)


# =========================================================
# FOOTER
# =========================================================

footer = tk.Label(
    root,
    text="Keep practicing and become a faster typist! ✨🌸",
    font=("Segoe Script", 13),
    bg=LIGHT_PINK,
    fg=TEXT
)

footer.pack(
    pady=15
)


# =========================================================
# RUN APPLICATION
# =========================================================

root.mainloop()