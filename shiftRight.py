# Bradley Cox - Homework 04, Problem 6

import sys

text = input("Enter a string of bits:")
shiftAmt = input("Enter the number of places to shift:")

try:
    shiftAmt = int(shiftAmt)
except ValueError:
    print("Error, shift value must be an integer.")
    sys.exit()

count = 0
while count < shiftAmt:
    text = text[-1] + text[:-1]
    count += 1

print(text)
