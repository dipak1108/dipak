#Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random

number_to_guess = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
while True:
    guess = input("Guess the number: ")


    try:
        guess = int(guess)
        if guess == number_to_guess:
            print("Congratulations! You guessed the number!")
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    except ValueError:
        print("Please enter a valid number.")
        continue


