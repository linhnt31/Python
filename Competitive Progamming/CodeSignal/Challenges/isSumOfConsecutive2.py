"""
-Link: https://app.codesignal.com/challenge/CY2qYcwMqPxp6Rsst
"""

#Solution 1:
def isSumOfConsecutive2(n):
    count = 0
    for i in range(1, n // 2 + 1):
        tmp = i
        for j in range(i + 1, n // 2 + 2):
            if tmp + j == n:
                count += 1
                break
            else:
                tmp += j
    return count

#Solution 2:
def isSumOfConsecutive3(n) -> int:
    count = 0
    
    for i in range(1, n // 2 + 1):
        tmp = 0
        j = i
        while tmp < n:
            tmp += j
            j += 1
        if tmp == n:
            count += 1
    return count