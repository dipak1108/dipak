#Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

import random

numberofdice = int(input("How many dice would you like to roll? "))
sum_ = 0
for i in range(numberofdice):
    roll = random.randint(1, 6)
    sum_ += roll

print(f"The sum of the rolls is: {sum_}")
