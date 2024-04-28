'''
Rock Paper Scissors

Author: Ishaan Reddy
'''
import random

user_wins = 0
champion_wins = 0

options = ['rock', 'paper', 'scissors']

# Introduction

print('Welcome to the Rock, Paper, Scissors Championship!')
print('Your opponent is the World Champion Rob Krugar')
print('The task is simple, beat the World Champion in a game of Rock, Paper, Scissors.')
print()

# Main Code

while True:
    print()
    user_input = input('Type Rock, Paper, Scissors or Q to quit: ').lower()
    if user_input == 'q' or user_input == 'quit':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    champion_selection = options[random_number]

    print(f'The World Champion selected: {champion_selection.capitalize()}')
        
    if user_input == champion_selection:
        print('A Tie!')
    elif user_input == 'rock' and champion_selection == 'scissors':
        print('You win!')
        user_wins += 1
    elif user_input == 'paper' and champion_selection == 'rock':
        print('You win!')
        user_wins += 1
    elif user_input == 'scissors' and champion_selection == 'paper':
        print('You win!')
        user_wins += 1
    else:
        print('You lost!')
        champion_wins += 1
        
if user_wins == 1 and champion_wins == 1:
    print(f'You won {user_wins} time!')
    print(f'The World Champion won {champion_wins} time!')
elif user_wins == 1 and champion_wins != 1:
        print(f'You won {user_wins} time!')
        print(f'The World Champion won {champion_wins} times!')
elif user_wins != 1 and champion_wins == 1:
    print(f'You won {user_wins} times!')
    print(f'The World Champion won {champion_wins} time!')
else:
    print(f'You won {user_wins} times!')
    print(f'The World Champion won {champion_wins} times!')

print('Thank you for playing!')
