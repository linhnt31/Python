"""
-Link: https://app.codesignal.com/tournaments/XMbCQfgcxkgbyi2aE
"""

#
def rightmostRoundNumber(inputArray):

    ans = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            ans = i

    return ans

#
def robotPath(instructions, bound):

    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0, -1]
    directions = 'LURD'
    x = 0
    y = 0

    for i in range(len(instructions)):
        dirIndex = 0
        for j in range(1, 4):
            if instructions[i] == directions[j]:
                dirIndex = j
        if (abs(x + dx[dirIndex]) <= bound
        and abs(y + dy[dirIndex]) <= bound):
            x += dx[dirIndex]
            y += dy[dirIndex]

    return [x, y]

#
def digitSum(n):
    if n < 10:
        return n
    return n % 10 + digitSum(n // 10)

#
def truncateString(s):
    while s:
        if s[0] in '369':
            s = s[1:]
        elif s[len(s)-1] in '369':
            s = s[:len(s)-1]
        elif ( int(s[0]) + int(s[len(s)-1])) % 3 == 0:
              s = s[1:len(s)-1]
        else:
              return s
    return ''
            
#
def sumOfPowers(n, divisor):
    res = []
    for i in range(1, n + 1):
        ans = 0
        while i % (divisor ** ans) == 0:
            ans += 1
        
        res.append(ans - 1)
    return sum(res)