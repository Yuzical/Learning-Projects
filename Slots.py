import random

MAX_LINES = 3
MAX_BET = 100 
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols)



def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():                                                #check if user input is a digit and not text
            amount = int(amount)
            if amount > 0:
                break                                        #if amount entered is greater than 2 the while loop breaks and continues on to return function
            else:
                print("Amount must be greater than 0.")     #if amount is less than 0 then else function starts
        else:
            print("Please enter a number.")                 #prompts user for number again
   
    return amount                                         #accepted number becomes amount function




def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():                                                #check if user input is a digit and not text
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:                      #checks if line is within current boundaries
                break                                        #if line input is less than or equal to lines variable and lines variable is less than or equal to MAX_LINES break loop
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")                 #prompts user for number again
   
    return lines                                            #accepted number becomes lines function



def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():                                                #check if user input is a digit and not text
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break                                        #if amount entered is greater than 2 the while loop breaks and continues on to return function
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")     #if amount is less than 0 then else function starts
        else:
            print("Please enter a number.")                 #prompts user for number again
   
    return amount   





def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
    
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
