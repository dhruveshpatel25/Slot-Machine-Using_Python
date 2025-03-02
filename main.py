import random

#no of lines to bet on
MAX_LINES=3

#maximum amount
MAX_BET=10000

#minimum amount
MIN_BET=100

ROWS=3
COLS=3

#no of symbols
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

#values of symbols
symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

#check winnings
def check_winnings(columns,bet,lines,values):
    winnings=0
    winnings_lines=[]

    #check horizontal lines
    for line in range(lines):

        #get symbol of first column
        symbol=columns[0][line]

        #check if all symbols in the line are same
        for column in columns:

            #check the other symbols
            symbol_to_check=column[line]

            #if symbols are not same
            if symbol_to_check!=symbol:
                break
        
        #if all symbols are same
        else:

            #add winnings
            winnings+=values[symbol]*bet

            #add winning line
            winnings_lines.append(line+1)
    return winnings,winnings_lines


#generate slot machine spin
def get_slot_machine_spin(rows,cols,symbol_count):

    #store all symbols
    all_symbols=[]

    #get all symbols
    for symbol,symbol_count in symbol_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #store columns
    columns=[]
    for _ in range(cols):
        column=[]

        #get symbols for each column
        current_symbols=all_symbols[:]
        for _ in range(rows):

            #get random symbol
            value=random.choice(current_symbols)

            #remove symbol from current symbols
            current_symbols.remove(value)

            #append symbol to column
            column.append(value)

        #append column to columns
        columns.append(column)

    return columns

#display slot machine spin
def print_slot_machine_spin(columns):

    #transpose columns
    for row in range(len(columns[0])):

        #print each row
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end=" ")
        print()

#deposit amount  
def deposit():
    while True:

        #input amount
        amount = input("Enter the amount you want to deposit: ")

        #check if amount is digit
        if amount.isdigit():

            #convert amount to integer
            amount=int(amount)

            #check if amount is greater than 0
            if amount > 0:
                break

            #if amount is less than 0
            else:
                print("Amount must be greater than 0")
        
        #if amount is not digit
        else:
            print('Enter number')

    return amount

def get_number_of_lines():
    while True:

        #input number of lines
        lines=input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + "): ")

        #check if lines is digit
        if lines.isdigit():

            #convert lines to integer
            lines=int(lines)

            #check if lines is between 1 and MAX_LINES
            if 1<=lines<=MAX_LINES:
                break

            #if lines is not between 1 and MAX_LINES
            else:
                print("Enter number between 1 and " + str(MAX_LINES))

        #if lines is not digit
        else:
            print('Enter number')
    
    return lines

def get_bet_amount():
    while True:

        #input bet amount
        bet=input("Enter the amount you want to bet on each line: ")

        #check if bet is digit
        if bet.isdigit():

            #convert bet to integer
            bet=int(bet)

            #check if bet is between MIN_BET and MAX_BET
            if MIN_BET<=bet<=MAX_BET:
                break

            #if bet is not between MIN_BET and MAX_BET
            else:
                print("Enter number between " + str(MIN_BET) + " and " + str(MAX_BET))
        
        #if bet is not digit
        else:
            print('Enter number')
    return bet

#spin the slot machine
def spin(balance):

    #get number of lines
    lines=get_number_of_lines()
    while True:

        #get bet amount
        bet=get_bet_amount()

        #total bet amount
        total_bet=bet*lines

        #check if balance is greater than total bet amount
        if total_bet<=balance:
            break

        #if balance is less than total bet amount
        else:
            print("You don't have enough balance to place this bet. Try again")
    
    print(f"You are betting {bet} on {lines} lines.Total bet amount is {bet*lines}")
    print("Balance: " + str(balance))
    print("Lines: " + str(lines))

    #get slot machine spin
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)

    #print slot machine spin
    print_slot_machine_spin(slots)

    #check winnings
    winning,winning_lines=check_winnings(slots,bet,lines,symbol_values)
    print(f"You won {winning}")
    print(f"Winning lines: {winning_lines}")
    return winning-total_bet


def main():

    #deposit amount
    balance=deposit()
    while True:

        #print current balance
        print(f"Current balance is {balance}")

        #ask if user wants to spin
        ans=input("Do you want to spin? (y/n): ")

        #if user doesn't want to spin
        if ans.lower()!="y":
            break

        #spin the slot machine
        balance+=spin(balance)

        #print the balance
        print(f"New balance is {balance}")

main()