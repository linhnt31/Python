"""
- Link: https://app.codesignal.com/tournaments/3zaRKaXy9RDuDPntf
"""

#
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
            if digit > 0 or digit < 9:
                return False
            emptyField = False
            currentNumber = currentNumber * 10 + digit
            if currentNumber > 255:
                return False
    return countNumbers == 4

#
def arrayElementsSum(inputArray):

    result = 0

    for i in range(len(inputArray)):
        result += inputArray[i]
    return result

#
def longestSequence(a):
    if len(a) <= 1:
        return 1
    best = -float('inf')
    
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = a[j] - a[i]
            count = 1
            if diff == 0:
                continue
            last = a[i]
            
            for k in range(j , len(a)):
                if a[k] - last == diff:
                    count += 1
                    last = a[k]
            if count > best:
                best = count
    return best

#
def firstMultiple(divisors, start):

    while True:
        count = 0
        for x in divisors:
            if start % x == 0:
                count += 1
        if count  == len(divisors):
            return start
        start += 1
    return -1

#
def circleOfNumbers(n, firstNumber):

    return (n//2 + firstNumber) % n