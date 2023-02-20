# Bradley Cox - Homework 04, Problem 3

import sys

inputFileName = input("Enter the input file name:")
outputFileName = input("Enter the output file name:")

if '.txt' not in inputFileName or '.txt' not in outputFileName:
    print("File name must include \'.txt\' suffix.")
    sys.exit()

shift = input("Enter the distance value:")

try:
    shift = int(shift)
except ValueError:
    print("Distance value must be an integer")
    sys.exit()

inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'w')

for line in inputFile:
    text = list(line)
    
    if '\n' in text:
        text.remove('\n')

    for i in range(len(text)):
        oldChar = ord(text[i])
        newChar = (oldChar + shift) % 128
        text[i] = chr(newChar)
    
    text = ''.join(text)
    
    outputFile.write(f"{text}\n")

inputFile.close()
outputFile.close()