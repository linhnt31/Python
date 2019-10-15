"""
-Link: https://app.codesignal.com/tournaments/XpdxBJ8HvrYD2xinP
-Link: https://app.codesignal.com/tournaments/8nQ8438FECzJzcg6W
"""

#
def applesDistribution(apples, boxCapacity, maxResidue):
    result = 0
    for i in range(1, boxCapacity + 1):
        if apples % i <= maxResidue:
            result += 1
    return result

#
def isLowerTriangularMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j > i and matrix[i][j] != 0:
                return False
    return True

#
def concatenateNumbers(a, b):

    return int(str(a) + str(b))

#
def numbersGrouping(a):
    res = []
    for x in a:
        if x % 10000 == 0:
            res.append(x // 10000)
        else:
            res.append(x // 10000 + 1)
    return len(a) + len(set(res))

#
def returnTwelve(number):
    while number < 12:
        return number
    return number

#
def differentValues(a, d):

    best = -1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = abs(a[j] - a[i ])
            if diff <= d and best < diff:
                best = diff

    return best

#
def improperFractionToMixed(a):

    return [a[0] // a[1], a[0] % a[1], a[1]]

#
def isIncreasingDigitsSequence(n):
    digits = list(map(int, str(n)))
    return sorted(digits) == digits and len(set(digits)) == len(digits)

#
def mixedFractionToImproper(a):

    return [a[0] * a[2] + a[1], a[2]]
