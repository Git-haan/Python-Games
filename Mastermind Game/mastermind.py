'''
Mastermind Game

Author: Ishaan Reddy
'''
import random

alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
tries = 10
code_length = 3

# Generates random 3 letter code

def generate_code():
    code = []

    for i in range(code_length):
        letter = random.choice(alphabet)
        code.append(letter)
    
    return code

# Asks for user input

def guess_code():
    while True:
        print()
        guess = input('Guess: ').upper().split(' ')

        if len(guess) != 3:
            print('You must guess 3 seperate letters!')
            continue

        for i in guess:
            if i not in alphabet:
                print(f'Invalid letter: {i}!')
                break
        else:
            break

    return guess

# Checks user input for correct and incorrect letters

def check_code(guess, real_code):
    letter_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for letter in real_code:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

    # zip decomposes guess and real into comparable tuples
    for guess_letter, real_letter in zip(guess, real_code): 
        if guess_letter == real_letter:
            correct_pos += 1
            letter_count[guess_letter] -= 1

    for guess_letter, real_letter in zip(guess, real_code): 
        if guess_letter in letter_count and letter_count[guess_letter] > 0:
            incorrect_pos += 1
            letter_count[guess_letter] -= 1

    return correct_pos, incorrect_pos

# Main code

def game():

    code = generate_code()
    i = 10

    for attempts in range(1, tries + 1):
        i -= 1
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print('The vault latch clicks open.')
            print('Infront of you is a pile of gold!')
            print()
            print(f'You guessed the code in {attempts} tries!')
            print('Thank you for playing!')
            break

        print()
        print(f'Correct Positions: {correct_pos} ')
        print(f'Incorrect Positions: {incorrect_pos} ')
        print(f'{i} tries left!')

    else:
        print()
        print('The cops arrived!')
        print()
        print(f'You ran out of tries, the code was: {code}')
        print('Thank you for playing!')
        print()

# Introduction

print('Welcome to a game called Mastermind.')
print('Your goal is to guess the correct code to unlock the vault full of gold!')

example = input('Do you want to see an example [yes/no]: ')
if example == 'yes' or example == 'y':
    print('The sequence should be 3 letters with a space inbetween')
    print('For example, your input could be: A A A')
else:
    pass

if __name__ == '__main__':
    game()