# Bradley Cox - Homework 04, Problem 1

import sys

text = input("Enter a message:")
shift = input("Enter the distance value:")

try:
    shift = int(shift)
except ValueError:
    print("Distance value must be an integer")
    sys.exit()

text = list(text)

for i in range(len(text)):
    oldChar = ord(text[i])
    newChar = (oldChar + shift) % 128
    text[i] = chr(newChar)

text = ''.join(text)
print(text)

