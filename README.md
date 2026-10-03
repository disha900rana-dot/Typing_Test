# 🎀 Typing Speed Test

A cute and interactive **Typing Speed Test application built with Python and Tkinter**.
The application allows users to test their typing speed, accuracy, number of words typed, and total time taken.

The project uses a **pink, blue, and yellow theme** with a cursive-style font to create a simple and friendly user interface. 🌸

---

## ✨ Features

* 🎀 Cute Pink, Blue & Yellow GUI
* ✍️ Cursive-style interface
* 🎲 Random typing sentences
* ⏱️ Automatic timer
* ⚡ Typing Speed in **Words Per Minute (WPM)**
* 🎯 Accuracy calculation
* 📝 Words typed counter
* 📊 Results displayed automatically
* 🔄 Start Again option
* ↻ Reset button
* 🚫 Typing automatically stops after completing the sentence
* 💻 Built using Python's built-in libraries

---

## 🖥️ Preview

The application provides four main results:

| Result           | Description                              |
| ---------------- | ---------------------------------------- |
| ⏱️ Time Taken    | Total time taken to type the sentence    |
| 📝 Words Typed   | Number of words entered by the user      |
| ⚡ Speed / Minute | Typing speed calculated in WPM           |
| 🎯 Accuracy      | Percentage of correctly typed characters |

Example:

```text
╭────────────────────────────╮
│        Your Results        │
├────────────────────────────┤
│ ⏱ Time Taken   12.45 sec  │
│ 📝 Words Typed      9      │
│ ⚡ Speed        43.37 WPM  │
│ 🎯 Accuracy       100.00%  │
╰────────────────────────────╯
```

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **Random** – Selects a random sentence
* **Time** – Measures typing time

No external Python packages are required.

---

## 📂 Project Structure

```text
Typing-Speed-Test/
│
├── typing_speed_test.py
└── README.md
```

---

## 🚀 How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/typing-speed-test.git
```

### 3. Open the Project

```bash
cd typing-speed-test
```

### 4. Run the Application

```bash
python typing_speed_test.py
```

The Typing Speed Test GUI will open.

---

## 🎮 How to Use

### Step 1 — Start the Test

Click:

```text
🎀 Start Test
```

A random sentence will appear.

### Step 2 — Start Typing

Begin typing the displayed sentence.

The timer automatically starts when you type your first character.

### Step 3 — Complete the Sentence

Once you finish typing the complete sentence, the application automatically calculates your results.

### Step 4 — View Results

The application displays:

```text
⏱ Time Taken
📝 Words Typed
⚡ Speed / Minute
🎯 Accuracy
```

### Step 5 — Try Again

Click:

```text
Start Again 🎀
```

to receive another random sentence.

You can also click:

```text
Reset ↻
```

to completely reset the test.

---

## ⚡ How WPM Is Calculated

The application calculates typing speed using **Words Per Minute (WPM)**.

First, the program calculates the time taken:

```python
time_taken = end_time - start_time
```

Then converts seconds into minutes:

```python
minutes = time_taken / 60
```

Finally:

```python
words_per_minute = word_count / minutes
```

For example:

```text
Words typed = 10
Time taken = 30 seconds

30 seconds = 0.5 minutes

WPM = 10 / 0.5
    = 20 WPM
```

---

## 🎯 Accuracy Calculation

Accuracy is calculated by comparing the characters typed by the user with the original sentence.

```python
correct_chars = sum(
    1
    for a, b in zip(user_input, test_sentence)
    if a == b
)
```

The percentage is then calculated using:

```python
accuracy = (
    correct_chars / len(test_sentence)
) * 100
```

For example:

```text
Correct characters = 50
Total characters = 50

Accuracy = 100%
```

---

## 🎨 Color Theme

The application uses a soft and cute color palette:

| Color     | Usage                         |
| --------- | ----------------------------- |
| 🌸 Pink   | Main theme and result cards   |
| 💙 Blue   | Sentence area and result card |
| 💛 Yellow | Instructions and speed card   |
| 🤍 White  | Main content areas            |

---

## 📋 Sample Sentences

The application randomly selects from sentences such as:

```text
The quick brown fox jumps over the lazy dog.
```

```text
A journey of a thousand miles begins with a single step.
```

```text
This is the way for us to reference the object of the class.
```

```text
Practice makes a person perfect and improves typing speed.
```

```text
Learning Python is fun when you practice every day.
```

---

## 💡 Future Improvements

Some features that can be added in future versions:

* 📈 Typing speed history
* 🏆 High-score system
* 👤 User profiles
* ⏳ 30-second and 60-second typing modes
* 🌐 Online leaderboard
* 📊 WPM performance graph
* 🔴 Live character highlighting
* 🟢 Correct/incorrect character colors
* 🔊 Sound effects
* 🌙 Dark mode
* 📅 Daily typing challenges

---

## 📜 License

This project is open-source and available for educational and personal use.

 
