# 🎰 Slot Machine Game

This is a **console-based Slot Machine Game** built using **Python**. The game allows the user to:
- Deposit money to their account.
- Bet on multiple lines (up to 3 lines).
- Spin the slot machine.
- Check winnings based on symbol combinations.
- Continue playing until the balance runs out or the user decides to quit.

---

## 📜 Features
- ✅ Deposit money to start the game.
- ✅ Bet on **1 to 3 lines**.
- ✅ Minimum bet amount: **₹100**
- ✅ Maximum bet amount: **₹10,000**
- ✅ Random slot machine spin with different symbols.
- ✅ Automatically calculates winnings based on the symbols.
- ✅ Displays winning lines and updated balance.
- ✅ Allows the user to keep playing until the balance is zero or they quit.

---

## 💸 Symbol Values and Probability
The game contains **4 different symbols**, each with different values and occurrence probabilities.

| Symbol | Occurrence Probability | Value (Multiplier) |
|---------|----------------------|---------------------|
| **A**   | Rare (2 times)         | **5x**              |
| **B**   | Uncommon (4 times)     | **4x**              |
| **C**   | Common (6 times)       | **3x**              |
| **D**   | Most Common (8 times)  | **2x**              |

### 💰 Example Payout Calculation
- If you bet ₹200 on **3 lines** and you get **3 A's** in one line, your payout will be:  
   **₹200 × 5 (A's value) = ₹1000**

- If you get **3 C's**, your payout will be:  
   **₹200 × 3 (C's value) = ₹600**

---

## 💻 How to Run the Game
### **1. Clone the Repository**
```bash
git clone https://github.com/dhruveshpatel25/Slot-Machine-Using_Python
```

### **2. Run the Python File**
Simply execute the Python file:
```bash
python main.py
```

### **3. Gameplay Flow**
1. **Deposit money** to start the game.
2. Select the **number of lines to bet on** (1 to 3).
3. Set the **bet amount per line**.
4. Spin the slot machine.
5. Check the winnings and balance.
6. Repeat or **quit** the game anytime.

---

## 💡 Game Rules
1. You can bet on **1 to 3 lines**.
2. The minimum bet amount is **₹100** and the maximum is **₹10,000**.
3. If you win, your balance increases based on the symbol multiplier.
4. If you lose, your balance decreases by the total bet amount.
5. Once your balance becomes zero, the game ends automatically.

---

## 📊 Winning Example
**Suppose you bet ₹500 on 3 lines and get:**
```
A | A | A     --> ₹500 * 5 = ₹2500
B | D | C
C | B | A
```
Your balance will increase by **₹2500** for line 1.

---

## 🧱 Code Structure
The game has the following main functions:

| Function Name       | Purpose                                                   |
|--------------------|------------------------------------------------------------|
| `deposit()`         | Allows the user to deposit money.                         |
| `get_number_of_lines()` | Asks the user how many lines they want to bet on.      |
| `get_bet_amount()`  | Accepts the bet amount within the valid range.             |
| `get_slot_machine_spin()` | Generates a random 3x3 slot machine result.         |
| `print_slot_machine_spin()` | Prints the slot machine output.                   |
| `check_winnings()`  | Calculates the winnings and returns the profit/loss.      |
| `spin()`            | Manages the game round and updates the balance.           |
| `main()`            | The main function to control the game flow.               |

---

## 🎉 Winning Lines
The game considers **horizontal winning lines** only.  
For example:  
```
A | A | A     <- Winning Line #1
B | D | C
C | B | A
```
In this case, you will win for **line 1**.

---

## 🔥 Limitations
- ❌ No diagonal winning lines are considered.
- ❌ The game stops when your balance reaches **zero**.
- ❌ Symbols and their probabilities are hardcoded.
- ❌ No graphical user interface (GUI) - it's console-based only.

---

## 📜 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## 💌 Contact
If you have any questions, suggestions, or feedback, feel free to reach out to me:  
- **GitHub**: https://github.com/dhruveshpatel25  
- **Email**: dhruu25@gmail.com    

---


