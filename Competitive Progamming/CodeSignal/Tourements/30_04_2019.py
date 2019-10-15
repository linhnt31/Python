"""
-Link: 
"""

#
def rangeBitCount(a, b):

    ans = 0
    for i in range(a, b + 1):
        t = i
        while t != 0:
            ans += t & 1
            t >>= 1

    return ans

#
def knapsackLight2(weight1, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return 'both'
    if min(weight1, weight2) > maxW:
        return 'none'
    if max(weight1, weight2) <= maxW:
        return 'either'
    if weight1 <= maxW:
        return 'first'
    return 'second'

#
def checkSameElementExistence(a, b):  

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return True
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return False

#Solution 2:
def checkSameElementExistence2(a, b):  
    return len(set(a) & set(b))
#
def kthDivisor(n, k):

    tmp = [x for x in range(1, n + 1) if n % x == 0]
    
    if k > len(tmp) or k < 0:
        return -1
    return tmp[k - 1]

#
def isLowerTriangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            if matrix[i][j]:
                return False
    return True