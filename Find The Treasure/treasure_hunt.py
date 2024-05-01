'''
Treasure Hunt Game

Author: Ishaan Reddy
'''
import random
import sys
import time

global name
global char

# Frontend

def loading_print(string): # function to print loading animation
    sys.stdout.write(string) # prints the string
    sys.stdout.flush() # flushes the buffer

loading_print('--------')
time.sleep(1)
loading_print('--------')
time.sleep(1)
loading_print('--------\n')
time.sleep(1)
print()
print('     TREASURE HUNT!      ')
print()
time.sleep(1)
loading_print('--------')
time.sleep(1)
loading_print('--------')
time.sleep(1)
loading_print('--------\n')
time.sleep(2)
print()
start = input('Type start or s to being: ').lower()
if start == 'start' or start == 's':
    print()
    pass
else:
    print('Goodbye.')
    quit()

print()
print('Welcome to the Lost Isles of Sundar!')
time.sleep(3)
print('You are on a quest to find the hidden treasure of Sundar.')
time.sleep(3)
print('You will have to navigate through the unknown terrain to find the long lost treasure.')
time.sleep(4)
print('Good luck! ')
print()

name = input('Enter Username: ')
print()
print(f'Welcome {name}!')
print()
print('Please choose your character: ')
print('1. Warrior [0] (No Help) \n2. Mage [x] (Casts A Useful Hint)\n3. Archer [*] (Double Shot Ability)\n')

char = input('Enter Input: ').lower()

if char == '0' or char == 'warrior' or char == 'w' or char == '1':
    char = '0'
    print('You have chosen the Warrior class!')
elif char == 'x' or char == 'mage' or char == 'm' or char == '2':
    char = 'X'
    print('You have chosen the Mage class!')
elif char == '*' or char == 'archer' or char == 'a' or char == '3':
    char = '*'
    print('You have chosen the Archer class!')
else: 
    while char not in ['0', 'x', '*']:
        print('Invalid Input! Please enter 0, x, or * to continue.')
        char = input('Enter Input: ').lower()
        if char == '0' or char == 'warrior' or char == 'w':
            char = '0'
            print('You have chosen the Warrior class!')
        elif char == 'x' or char == 'mage' or char == 'm':
            char = 'X'
            print('You have chosen the Mage class!')
        elif char == '*' or char == 'archer' or char == 'a':
            char = '*'
            print('You have chosen the Archer class!')

print()
back_story = input('Would you like to read the backstory of the Lost Isles of Sundar? [yes/no]: ').lower()
if back_story == 'yes' or back_story == 'y':
    print()
    print('Long ago, the Lost Isles of Sundar were a prosperous land, filled with riches and treasures.')
    time.sleep(4)
    print('The people of Sundar were known for their kindness and generosity.')
    time.sleep(5)
    print('But one day, the land was attacked by the evil sorcerer.')
    time.sleep(4)
    print('The people of Sundar were forced to flee their homes and hid the treasure in a secret location.')
    time.sleep(6)
    print('The treasure of Sundar has been lost for centuries.')
    time.sleep(4)
    print('You are the chosen one, destined to find the treasure and restore prosperity to the Lost Isles of Sundar.')
    time.sleep(6)
    print()
else:
    print()

instructions = input('Would you like to read the instructions of the game? [yes/no]: ').lower()
if instructions == 'yes' or instructions == 'y':
    print()
    print('Instructions:')
    print('The Isles of Sundar can be seen as a 5x5 grid.')
    print('The treasure is hidden amidst the grid.')
    print('The player has to guess the right row and column of the treasure')
    print('The player has 10 guesses.')
    print('Remember each class has unique perks that will help finding the treasure.')
    time.sleep(4)
else:
    print()
    print('Your journey begins now!')
    print()

# Backend

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

def main():
    play_again = 'yes'
    while play_again == 'yes' or play_again == 'y':
        board = []
        for x in range(5):
            board.append(["[ ]"] * 5)

        print_board(board)

        treasure_row = random_row(board)
        treasure_col = random_col(board)

        attempts = 0

        if char == '*':
            placeholder = 20
            print()
            print(f'{name} Activates Double Shot Ability')
            print('Guesses Double From 10 To 20')
        else:
            placeholder = 10

        for attempt in range(placeholder):
            print("Attempt", attempt + 1)
            guess_row = input("Guess Row: ")
            guess_col = input("Guess Col: ")

            while True:
                try:
                    guess_row = int(guess_row) - 1
                    guess_col = int(guess_col) - 1
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    guess_row = input("Guess Row: ")
                    guess_col = input("Guess Col: ")


            if guess_row == treasure_row and guess_col == treasure_col:
                print(f'Congratulations {name}! You have found the treasure!')
                print('The people of Sundar thank you!')
                break
            else:
                if guess_row not in range(5) or guess_col not in range(5):
                    print("Oops, that seems to be in the ocean.")
    
                elif board[guess_row][guess_col] == f"[{char}]":
                    print("Oops, you guessed that one already.")
                else:
                    print("You missed the treasure!")
                    board[guess_row][guess_col] = f"[{char}]"
                print_board(board)
            attempts += 1
    
            if char == 'X' and attempts == 5:
                print()
                print(f'{name} casts a hint: The treasure is located on row {treasure_row + 1}')
    
        if attempts == 10 or attempts == 20:
            print("Game Over! The treasure was at row", treasure_row + 1, "and column", treasure_col + 1)
            print("You have failed the people of Sundar!")
        print()
        play_again = input('Would you like to play again? [yes/no]: ').lower()
    print('Thank you for playing!')

if __name__ == "__main__":
    main()
