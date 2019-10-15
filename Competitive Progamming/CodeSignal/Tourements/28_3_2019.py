'''
- Link: https://app.codesignal.com/tournaments/jZ7x87bJfNWSajXgp
'''

#
def triangleExistence(sides):

    sides = sorted(sides)

    if sides[0] + sides[1] > sides[2]:
        return False
    return False

#
def arrayConversion(inputArray):

    operation = 1
    while len(inputArray) > 1:
        newArray = []
        for i in range(0, len(inputArray), 2):
            if operation % 2 == 1:
                newArray.append(inputArray[i] + inputArray[i + 1])
            else:
                newArray.append(inputArray[i] * inputArray[i + 1])
        inputArray = newArray
        operation += 1

    return inputArray[0]

#
def maxSubmatrixSum(matrix, n, m):

    lx = len(matrix)
    ly = len(matrix[0])
    res = -float('inf')
    
    for x in range(lx - n + 1):
        for y in range(ly - m + 1):
            res = max(res, sum(sum(matrix[i][y:y+m]) for i in range(x, x+n)))
    return res

#
def fibonacciNumber(n):
    f0 = 0
    f1 = 1
    res = 1
    for _ in range(1, n):
        res = f0 + f1
        f0 = f1
        f1 = res
    return res
        

#
def maxFraction(numerators, denominators):
    max_ = numerators[0] / denominators[0]
    ind = 0
    for i in range(1, len(numerators)):
        if max_ < numerators[i] / denominators[i]:
            max_ = numerators[i] / denominators[i]
            ind = i
    return ind
