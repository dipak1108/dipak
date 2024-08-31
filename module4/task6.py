import random

N = 1000000
n = 0
iterator = 0

while iterator < N:
    x = random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x ** 2 + y ** 2 < 1:
        n += 1
    iterator += 1

print(4 * n / N)