'''
-Link: https://app.codesignal.com/tournaments/ja35WvdHXAwDotRGN
-Link: https://app.codesignal.com/tournaments/NzqCftTaYEFRm52og
-Link: https://app.codesignal.com/tournaments/sTWy7LPKy8Dmxhjfw
'''

#
def isTandemRepeat(inputString):

    length = len(inputString)
    if length % 2 == 1:
        return False

    for i in range(length // 2):
        if inputString[i] != inputString[i + len]:
            return False

    return True

#
def pointInLine(point, line):
    return point[0] * line[0] + point[1]*line[1] + line[2] == 0

#
def sumOfTheAngles(n):
    return (n - 2) * 180

#
import string
def caseUnification(inputString):
    count1 = 0
    count2 = 0
    for ch in inputString:
        if ch in string.ascii_lowercase:
            count1 += 1
        elif ch in string.ascii_uppercase:
            count2 += 1
            
    return inputString.lower() if count1 > count2 else inputString.upper()

#
def josephusProblem(n, k):

    removed = []
    currentPerson = 0

    for i in range(n):
        removed.append(False)

    for i in range(1, n):
        skipped = 0
        while skipped < k - 1:
            if not removed[currentPerson]:
                skipped += 1
            currentPerson = (currentPerson + 1) % n
        while removed[currentPerson]:
            currentPerson = (currentPerson + 1) % n
        removed[currentPerson] = True

    for i in range(n):
        if not removed[i]:
            return i + 1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#
def fractionReducing(fraction):

    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    commonDivisor = gcd(fraction[0], fraction[1])
    fraction[0] /= commonDivisor
    fraction[1] /= commonDivisor

    return fraction

#
def isLowerTriangularMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j > i and matrix[i][j] != 0:
                return False
    return True

#
def isIdentityMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

#
import string
def latinLettersSearchRegExp(input):
    
    for ch in input:
        if ch in string.ascii_letters:
            return True
    return False

""""""""""""""""""""""""""""""""""""""""""

#
def differentSubstrings(inputString):

    substrings = []
    result = 1

    for i in range(len(inputString)):
        for j in range(i - 1, len(inputString) + 1):
            substrings.append(inputString[i:j])
    substrings.sort()
    for i in range(1, len(substrings)):
        if substrings[i] != substrings[i - 1]:
            result += 1

    return result

#
def countWaysToChangeDigit(value):
    answer = 0
    while value > 0:
        answer += 9 - value % 10
        value //= 10
    return answer

#
def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 1
    up = upSpeed - downSpeed
    
    while upSpeed < desiredHeight:
        day += 1
        upSpeed += up
    return day

#
def leastFactorial(n):
    res = 1
    tmp = 1
    while res < n:
        res = res * tmp
        tmp += 1
    return res

#
def rounders(n):

    res = []
    add = 0
    
    while n > 10:
        if (n % 10 + add) < 5:
            add = 0
        else:
            add = 1
        res.append('0')
        n //= 10
    res.append(str(n + add))
    res = res[::-1]
    return int("".join(res))