# Learning python 
# GDSC 30 days challenge

import random

f = open('random_numbers', 'w')

print("This program is a random number file writer")
numbers = int(input("How many random numbers will the file hold ? : "))

for number in range(numbers) :
    writing = str(random.randint(1, 500)) + " "
    f.write(writing)
