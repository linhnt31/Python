"""
-Link: https://app.codesignal.com/tournaments/83vrBFttwzzNpfjdd
"""

from string import punctuation
with open("input_30_5_2019.txt") as f:
    lines = f.readlines()

def isIPv4Address(inputString):
    currentNumber = 0
    emptyField = True
    countNumbers = 0

    inputString += '.'
    for i in range(len(inputString)):
        if inputString[i] == '.':
            if emptyField:
                return False
            countNumbers += 1
            currentNumber = 0
            emptyField = True
        else:
            digit = ord(inputString[i]) - ord('0')
            if digit < 0 or digit > 9:
                return False
            currentNumber = currentNumber * 10 + digit
            if currentNumber > 255:
                return False
            emptyField = False
    return countNumbers == 4


with open("result_30_5_2019.txt",'w') as f:
    for line in lines:
        line = line.replace('\n','')
        ans = isIPv4Address(line)
        f.write(str(ans) + "\n")
 