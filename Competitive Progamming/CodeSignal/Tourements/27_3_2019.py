'''
- Link: https://app.codesignal.com/tournaments/X5LjqZp8FLRtwauFP
- Link: https://app.codesignal.com/tournaments/hE5eBmdkF592mLcam
'''

#
def alternatingSums(a):
    team1 = 0
    team2 = 0
    for i in  range(0, len(a), 2):
        team1 += a[i]
    for i in range(1, len(a), 2):
        team2 += a[i]
    result = [team1, team2]
    return result

#
def checkSameElementExistence(arr1, arr2):
    return len(set(arr1) - set(arr2)) != len(set(arr1))

#
def firstNotDivisible(divisors, start):
    while True:
        count = 0
        for x in divisors:
            if start % x != 0:
                count += 1
        if count == len(divisors):
            return start
        start += 1

#
def leapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

#
def isLowerTriangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j]:
                return False
    return True

#
def sequencePeakElement(sequence):
    left = 1
    right = len(sequence) - 2
    while left < right:
        middle = (left + right) // 2
        if sequence[middle] > max(sequence[middle - 1], sequence[middle + 1]):
            left = right = middle
            break
        if sequence[middle - 1] < sequence[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return sequence[left]

#
def makeArrayConsecutive(sequence):
    res = []
    for x in range(min(sequence), max(sequence)+ 1):
        if x not in sequence:
            res.append(x)
    return res
#
def properNounCorrection(noun):
    return noun[0].upper() + noun[1:].lower()
