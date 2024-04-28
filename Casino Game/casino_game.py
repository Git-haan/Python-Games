'''
Casino Game

Author: Ishaan Reddy
'''
import random
import time
import copy

MAX_LINES = 3
MAX_WAGER = 1000000
MIN_WAGER = 1
MIN_DEPOSIT = 10
MAX_DEPOSIT = 10000000

REEL = ['O', '#', 'X']

def spin():
    random_reel = []

    for i in REEL:
        random_reel = [random.choice(REEL), random.choice(REEL), random.choice(REEL)]
    return random_reel

def print_machine(M):
    
    print()
    print('---- SLOT MACHINE ----')
    print('----------------------')

    for row in machine:
        for element in row:
            print('|', element, '|', end ='\t')
        print()
        time.sleep(2)
    print()

def check_list(M, lines):

    count = 0

    if lines == 1:
        for i in range(len(M) - 2):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1
    elif lines == 2:
        for i in range(len(M) - 1):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1
    elif lines == 3:
        for i in range(len(M)):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1

    return count

def deposit():
    while True:
        amount = input('Enter the amount to deposit: $')

        if amount.isdigit():
            amount = int(amount)

            if 10000000 > amount >= 10:
                break
            else:
                print('--------------------------------------------------------------------------------')
                print(f'WARNING: The casino mandates a deposit between ${MIN_DEPOSIT} - ${MAX_DEPOSIT}.')
                print('--------------------------------------------------------------------------------')
                print()
                continue

        else:
            print('----------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('----------------------------------------')
            print()
            continue

    return amount

def get_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1 - {MAX_LINES}): ')

        if lines.isdigit():
            lines = int(lines)

            if lines > 0:
                pass
            else:
                print('-------------------------------------------------')
                print('WARNING: Amount must be greater than 0!')
                print('-------------------------------------------------')
                print()
                continue

            if lines <= MAX_LINES:
                break
            else:
                print('-------------------------------------------------')
                print(f'WARNING: Maximum lines to bet on is {MAX_LINES}!')
                print('-------------------------------------------------')
                print()
                continue
        else:
            print('-------------------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('-------------------------------------------------')
            print()
            continue

    return lines

def get_bet():
    while True:
        bet = input('Enter the amount to bet on each line: $')

        if bet.isdigit():
            bet = int(bet)

            if bet >= MIN_WAGER:
                pass
            else:
                print('---------------------------------------------------')
                print(f'WARNING: The casino mandates a minumum bet of ${MIN_WAGER}.')
                print('---------------------------------------------------')
                print()
                continue

            if bet <= MAX_WAGER:
                break
            else:
                print('---------------------------------------------------')
                print(f'WARNING: The casino mandates a maximum bet of ${MAX_WAGER}.')
                print('---------------------------------------------------')
                print()
                continue
        else:
            print('----------------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('----------------------------------------------')
            print()
            continue

    return bet

def game():
    print('-------------------------------------------------------------------')
    print('Welcome to CASINO ROYALE: A virtual slot machine to test your luck!')
    print('To begin, please deposit a minimum of $10 to play!')
    print()
    
    balance = deposit()
    orignal_balance = copy.copy(balance)

    x = False
    while x == False:
        global machine
        machine = [spin(), spin(), spin()] # Initializes a random machine
        # print(machine) if you want to see the machine before the game starts

        print(f'Your current balance is: ${balance}')
        print()
        lines = get_lines()
        
        while True: 
            bet = get_bet()

            if (bet*lines) > balance:
                print('-------------------------------------------------')
                print(f'WARNING: You do not enough funds to bet ${bet} on each line!')
                print('-------------------------------------------------')
                print()
            else:
                break

        print()
        print('-------------------------------------------------')
        print(f'You are betting ${bet} on {lines} lines.')
        print(f'Your total betting valuation: ${bet * lines}')
        print('-------------------------------------------------')
        print()
        confirm = input('Please confirm this valuation [YES/NO]:').lower()
        print()

        if confirm == 'yes' or confirm == 'y':
            x = True
        elif confirm == 'no' or confirm == 'n':
            print()
            continue
        else:
            print('-------------------------------------------')
            print(f'WARNING: {confirm} is not a valid option.')
            print('-------------------------------------------')
            print()
            continue
    
        while True:
            spin_input = input('Please hit "ENTER" to activate the machine: ').lower()
            if spin_input != '':
                print('---------------------------------------------------')
                print('WARNING: Please hit "ENTER" to activate the machine.')
                print('---------------------------------------------------')
                print()
                continue
            else:
                print_machine(machine)
                break

        count = check_list(machine, lines)

        if count < 0:
            balance -= (abs(bet * count))
            print('-------------------------------------------------')
            print(f'Total Loss: ${abs(bet * count)}!')
            print('-------------------------------------------------')
            print()
            
        elif count == 0:
            print('-------------------------------------------------')
            print('You Drew Even!')
            print('-------------------------------------------------')
            print()
        else:
            balance += (count * bet)
            print('-------------------------------------------------')
            print(f'Congratulations! Total Win: ${count * bet}!')
            print('-------------------------------------------------')
            print()
    
        while True:
            play_again = input('Would you like to play again? [YES/NO]: ').lower()

            if play_again == 'yes' or play_again == 'y':
                x = False
                break
            elif play_again == 'no' or play_again == 'n':
                break
            else:
                print('Please type a valid input.')
                continue

    print()
    print('Thank you for playing at CASINO ROYALE!')
    print('----------------------------------------')
    print(f'Your final balance is: ${balance}')
    if balance > 0:
        print(f'Profit: ${balance - orignal_balance}!')
    else:
        print(f'Loss: ${orignal_balance - balance}!')
    print('----------------------------------------')

if __name__ == '__main__':
    game()
