"""Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6."""

from random import randint, randrange, random

num1 = str(random())

print(f'Code 1: {num1[2:5]}')

num4 = randint(1,6)
num5 = randint(1,6)
num6 = randint(1,6)
num7 = randint(1,6)

print(f'Code 2: {num4}{num5}{num6}{num7}')
