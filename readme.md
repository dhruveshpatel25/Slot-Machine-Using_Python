# Slot Machine Game

## Description
This is a simple command-line slot machine game written in Python. The game allows users to deposit money, place bets on multiple lines, and spin the slot machine to try their luck.

## Features
- Deposit money before playing
- Choose the number of lines to bet on (1 to 3)
- Set a bet amount within a specified range
- Spin the slot machine and win based on matching symbols
- Display winnings and update balance after each spin

## Requirements
- Python 3.x

## How to Run
### Manually Copy-Paste
1. Open your project folder.
2. Create a new file named `README.md`.
3. Open `README.md` in a text editor (VS Code, Notepad++, or any IDE).
4. Copy the content from this README.
5. Paste it into `README.md`.
6. Save the file.

### Using Command Line
If you're using a terminal (Command Prompt, Git Bash, or Terminal):

1. Navigate to your project directory:
   ```sh
   cd path/to/your/project
   ```
2. Create a `README.md` file:
   ```sh
   touch README.md
   ```
3. Open it in a text editor (e.g., VS Code):
   ```sh
   code README.md
   ```
4. Paste the README content and save the file.

### Using Python Script
If you want to create a `README.md` file directly using Python:

```python
readme_content = """# Slot Machine Game

## Description
This is a simple command-line slot machine game written in Python. The game allows users to deposit money, place bets on multiple lines, and spin the slot machine to try their luck.

## Features
- Deposit money before playing
- Choose the number of lines to bet on (1 to 3)
- Set a bet amount within a specified range
- Spin the slot machine and win based on matching symbols
- Display winnings and update balance after each spin

## Requirements
- Python 3.x

## How to Run
1. **Clone the repository (if applicable):**
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Run the Python script:**
   ```sh
   python slot_machine.py
   ```

## How to Play
1. Enter the amount you want to deposit.
2. Choose the number of lines to bet on (between 1 and 3).
3. Enter the bet amount per line (between 100 and 10,000).
4. The total bet amount is calculated as `bet * lines`.
5. The slot machine will spin and display the outcome.
6. If you win, your winnings are added to the balance; otherwise, the bet amount is deducted.
7. You can continue playing until you run out of balance or choose to quit.

## Game Rules
- Symbols have different probabilities and values:
  - `A` (Highest Value, Rare)
  - `B`
  - `C`
  - `D` (Lowest Value, Most Common)
- A win occurs when all symbols in a horizontal line match.
- Payout is determined by the symbol value multiplied by the bet amount.

## Example Gameplay
```
Enter the amount you want to deposit: 5000
Enter the number of lines to bet on (1-3): 2
Enter the amount you want to bet on each line: 200
You are betting 200 on 2 lines. Total bet amount is 400
Balance: 5000
Lines: 2

Slot Machine Spin:
A | B | C
A | A | A
C | D | B

You won 1000
Winning lines: [2]
New balance is 5600
```

## License
This project is for educational purposes and is free to use.

## Author
- Your Name (or GitHub username)
"""

# Create and write to README.md
with open("README.md", "w") as file:
    file.write(readme_content)

print("README.md file created successfully!")
```

Run this script in the same directory as your project, and it will create `README.md` for you.

## License
This project is for educational purposes and is free to use.

## Author
- Your Name (or GitHub username)

