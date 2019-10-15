"""
-Link: https://app.codesignal.com/tournaments/xEd53zrW9yq9FmDoF
"""

#
def isIdentityMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] != 1 and i == j
              or matrix[i][j] and i != j):
                return False
    return False

#
def chessBoardCellColor(cell1, cell2):

    def getX(pos):
        return ord(pos[0]) - ord('A')
    def getY(pos):
        return ord(pos[0]) - ord('1')

    sum1 = getX(cell1[0]) + getY(cell1[1])
    sum2 = getX(cell2[0]) + getY(cell2[1])
    if sum1 % 2 == sum2 % 2:
        return True
    return False

#
def reflectString(a):

    res = []
    
    for x in a:
        res.append(chr(219 - ord(x)))
    return "".join(res)

#
def numberOfOperations(a, b):

    if b > a:
        return numberOfOperations(b, a)
    if a % b == 0:
        return 1 + numberOfOperations(a // b, b)
    return 0