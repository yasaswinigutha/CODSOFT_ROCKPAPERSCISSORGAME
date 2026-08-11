# CODSOFT_ROCKPAPERSCISSORGAME
# 🎮 Rock-Paper-Scissors Game

A simple and interactive **Rock-Paper-Scissors game built using Python**, where the user plays against the computer. The computer randomly selects rock, paper, or scissors, and the winner is determined based on the standard game rules.

## 📌 Features

* 🎮 Interactive gameplay
* 👤 User input for selecting Rock, Paper, or Scissors
* 🤖 Random computer selection
* 🏆 Automatic winner determination
* 📊 Score tracking
* 🔄 Play multiple rounds
* ✅ Input validation
* 🤝 Tie detection
* 🏅 Final score and overall winner display

## 🕹️ Game Rules

| User Choice | Computer Choice | Winner |
| ----------- | --------------- | ------ |
| Rock 🪨     | Scissors ✂️     | User   |
| Scissors ✂️ | Paper 📄        | User   |
| Paper 📄    | Rock 🪨         | User   |
| Same Choice | Same Choice     | Tie    |

### Basic Rules

* 🪨 **Rock beats Scissors**
* ✂️ **Scissors beats Paper**
* 📄 **Paper beats Rock**
* Same choices result in a **Tie**

## 🛠️ Technologies Used

* **Python**
* **Random Module**

## 📂 Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 3. Open the Project Folder

```bash
cd Rock-Paper-Scissors
```

### 4. Run the Program

```bash
python rock_paper_scissors.py
```

## 🎯 How to Play

When the program starts, you will see:

```text
Choose one:
1. Rock
2. Paper
3. Scissors

Enter your choice (1-3):
```

Enter:

```text
1 → Rock
2 → Paper
3 → Scissors
```

The computer will randomly select its choice, and the program will display the result.

## 💻 Sample Output

```text
=============================================
       ROCK-PAPER-SCISSORS GAME
=============================================

Game Rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock

Choose one:
1. Rock
2. Paper
3. Scissors

Enter your choice (1-3): 1

-----------------------------
Your choice     : rock
Computer choice : scissors
Result          : You Win! 🎉
-----------------------------

Current Score:
You      : 1
Computer : 0
Ties     : 0

Do you want to play again? (yes/no): yes
```

## 📊 Score Tracking

The game keeps track of:

* **Your Score**
* **Computer Score**
* **Number of Ties**

At the end of the game, the overall winner is displayed.

## 👩‍💻 Author

**Yasaswini Gutha**
