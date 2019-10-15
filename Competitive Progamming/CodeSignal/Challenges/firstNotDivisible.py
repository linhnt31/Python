"""
- Link: https://app.codesignal.com/challenge/zxZqdshbxbfvaMKHf
"""

def firstNotDivisible(divisors, start):

    tmp = start
    
    while tmp >= start:
        count = 0
        for x in divisors:
            if tmp % x == 0:
                count += 1
        if count == 0:
            return tmp
        tmp += 1