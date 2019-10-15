'''
- Link 1: https://app.codesignal.com/tournaments/QWzsoFM36guEtCQkM
- Link 2: https://app.codesignal.com/tournaments/Ho9SHRFd55NX4CNsQ
- Link 3: https://app.codesignal.com/tournaments/fmWkeZA8eQRHZD6YB
'''
import math
#
def properOrImproper(a):

    if abs(a[0] / a[1]) <= 1:
        return 'Proper'
    return 'Improper'

#
def mergeSort(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left >= right - 1:
            return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence


#
def depositProfit(deposit, rate, threshold):
    res = 0
    
    while deposit < threshold:
        deposit += (deposit * rate)/100
        res += 1
    return res

#
def mySubstring(inputString, l, r):
    return inputString[l:r+1]


#
def findTheRemainder(a, b):
    return a % b

#
def quadraticEquation(a, b, c):

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return []
    if discriminant == 0:
        return [- b / (2 * a)]
    roots = []
    roots.append((- b - math.sqrt(discriminant) ) / (2 * a))
    roots.append((- b + math.sqrt(discriminant) ) / (2 * a))
    if roots[0] < roots[1]:
        tmp = roots[1]
        roots[1] = roots[0]
        roots[0] = tmp
    return roots


#
def isDivisibleBy3(inputString):

    digitSum = 0
    leftBound = ord('0')
    rightBound = ord('9')
    answer = []
    mask = list(inputString)
    asteriskPos = -1

    for i in range(len(mask)):
        if (leftBound <= ord(mask[i]) and ord(mask[i]) <= rightBound):
            digitSum += ord(mask[i]) - leftBound
        else:
            asteriskPos = i

    for i in range(10):
        if (digitSum + i) % 3 == 0:
            mask[asteriskPos] = chr(leftBound + i)
            answer.append(''.join(mask))

    return answer


#
def extraNumber(a, b, c):
    if a == b:
        return c 
    elif a == c:
        return b 
    return a

#
def integerToStringOfFixedWidth(number, width):
    str_numb = str(number)
    res = []
    
    if len(str_numb) < width:
        for _ in range(0, width - len(str_numb)):
            res.append('0')
        res.append(str_numb)
        return "".join(res)
    return str_numb[-width + len(str_numb)::]


#
def lastDigitRegExp(inputString):
    for i in range(len(inputString) - 1, -1, -1):
        x = inputString[i]
        if x >= '0' and x < '9':
            return x
    
    return ''

def lastDigitRegExp1(inputString):
    inputString = reversed(inputString)
    
    for x in inputString:
        if x.isdigit():
            return x
    
    return ''

#
def isInRange(a, b, c):
    if a <= b and b <= c:
        return True
    return False

#
def checkData(inputString):
    return len(inputString) == 3

#
def adjacentElementsProduct(inputArray):
    max_ = -(math.inf)
    for i in range(0, len(inputArray)-1):
        max_ = max(max_, inputArray[i] * inputArray[i + 1])
    
    return max_
#
#