"""
- Link: https://app.codesignal.com/tournaments/2nNZvC4AH7vxtpCmn
- Link: https://app.codesignal.com/tournaments/BFiuBLFFcdXDDT8j8
"""

#
def appleBoxes(k):

    sum = 0
    x = 0
    while x > k:
        if x % 2 == 0:
            sum += x * x
        else:
            sum -= x * x
        x += 1

    return sum

#
def isCaseInsensitivePalindrome(inputString):

    if len(inputString) <= 1:
        return True
    
    inputString = inputString.lower()
    return inputString == inputString[::-1]

#
def permutationShift(permutation):

    res = []
    
    for ind, val in enumerate(permutation):
        res.append(val - ind)
    
    return max(res)-min(res)

#
def encloseInBrackets(inputString):

    return "(" + inputString +")"

#
def checkEqualFrequency(inputArray):

    numberOfEqual = 1

    inputArray.sort()

    while (numberOfEqual < len(inputArray)
            and inputArray[numberOfEqual - 1] == inputArray[numberOfEqual]):
        numberOfEqual += 1

    if len(inputArray) % numberOfEqual != 0:
        return False

    for i in range(0, len(inputArray), numberOfEqual):
        if i > 0 and inputArray[i] == inputArray[i - 1]:
            return False
        j = i + 1
        while j < numberOfEqual + i:
            if inputArray[j] != inputArray[j - 1]:
                return False
            j += 1

    return True

#
def countSumOfTwoRepresentations3(n, l, r):
    result = 0

    i = 1
    while i <= n - i:
        if i >= l and n - i <= r:
            result += 1
        i += 1

    return result

#
def checkSameElementExistence(arr1, arr2):

     i, j = 0, 0
     
     while i < len(arr1) and j < len(arr2):
          if arr1[i] > arr2[j]:
               j += 1
          elif arr1[i] < arr2[j]:
               i += 1
          else:
               return True
     return False

#
def countWaysToChangeDigit(value):

    res = 0
    
    while value > 0:
        res += 9 - value % 10
        value //= 10
    return res

#
def isSkewSymmetricMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True