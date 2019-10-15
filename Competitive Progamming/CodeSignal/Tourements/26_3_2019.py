'''
- Link: https://app.codesignal.com/tournaments/kR7CC7hMbdjfEzxuS
- Link: https://app.codesignal.com/tournaments/FcHjw3F89S4S7RbYd
'''

#
def sumOfTheAngles(n):
    result = 180 * n
    result -= 180 * 2
    return result

#
def theJanitor(word):
    res = [0] * 26
    
    for i in set(word):
        res[ord(i) - 97] = len(word) - word.index(i) - word[::-1].index(i)
    return res

#
def orthogonalLines(line1, line2):
    return line1[0] * line2[0] + line1[1] * line2[1] == 0

#
def properOrImproper(a):
    if abs(a[0] / a[1]) < 1:
        return 'Proper'
    return 'Improper'

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
def allLongestStrings(inputArray):
    max_len = max([len(i) for i in inputArray])
    return [i for i in inputArray if len(i) == max_len]

#
def isDivisibleBy6(inputString):

    digitSum = 0
    leftBound = ord('0')
    rightBound = ord('9')
    answer = []
    mask = list(inputString)
    asteriskPos = -1

    for i in range(len(mask)):
        if (leftBound <= ord(mask[i]) and
          ord(mask[i]) <= rightBound):
            digitSum += ord(mask[i]) - leftBound
        else:
            asteriskPos = i

    for i in range(10):
        if (digitSum + i) % 3 == 0:
            mask[asteriskPos] = chr(leftBound + i)
            if (ord(mask[len(mask) - 1]) - leftBound) % 2 == 0:
                answer.append(''.join(mask))

    return answer

