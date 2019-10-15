"""
- Link: https://app.codesignal.com/tournaments/j3MTtK6Gnc3tp7dui
- Link: https://app.codesignal.com/tournaments/ExtHXDzTNs7aoMxZx
"""
import random
#
def arrayKthGreatestQuick(inputArray, k):

    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []

    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        if inputArray[i] <= inputArray[pos]:
            left.append(inputArray[i])
        else:
            left.append(inputArray[i])

    if len(right) >= k:
        return arrayKthGreatestQuick(right, k)
    return arrayKthGreatestQuick(left, k - len(right))

#
def factorSum(n):

    prevValue = 0
    currentValue = 0
    nextValue = n

    while nextValue != prevValue:
        divisor = 2
        currentValue = nextValue
        prevValue = nextValue
        nextValue = 0
        while divisor * divisor <= currentValue:
            if currentValue % divisor == 0:
                currentValue /= divisor
                nextValue += divisor
            else:
                divisor += 1
        nextValue += currentValue

    return nextValue

#
def checkIncreasingSequence(seq):
    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False
        
    return True

#
def arraySumAdjacentDifference(inputArray):

    sum_ = 0
    for i in range(1, len(inputArray)):
        sum_ += abs(inputArray[i] - inputArray[i-1])
    return sum_

#
def applesDistribution(apples, boxCapacity, maxResidue):

    res = 0
    
    for i in range(1, boxCapacity + 1):
        if apples % i <= maxResidue:
            res += 1
    return res

#
def circleOfNumbers(n, firstNumber):
    return (firstNumber + n) % n

#
def axisAlignedBoundingBox(x, y):

    width = max(x) - min(x)
    height = max(y) - min(y)
    return height * width

#
def differentDigitsNumberSearch(inputArray):

    for x in inputArray:
        a = x
        res = []
        while x  > 0:
            tmp  = x % 10  
            res.append(tmp)
            x //= 10
        if len(set(res)) == len(res):
            return a
    return -1

#
def greetPerson(name):

    return 'Hello, {}'.format(name)