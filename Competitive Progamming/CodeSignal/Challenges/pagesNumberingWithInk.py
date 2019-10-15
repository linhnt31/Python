"""
-Link: https://app.codesignal.com/challenge/xDgfotwk4owqaGyTb
"""

def pagesNumberingWithInk(current, numberOfDigits):
    digitsInCurrentNum = appear(current)
    
    while numberOfDigits >= digitsInCurrentNum:
        numberOfDigits -= digitsInCurrentNum
        current += 1
        digitsInCurrentNum = appear(current)
    return current - 1

def appear(a):
    if a < 10:
        return 1
    
    count = 0
    while a > 0: 
        count += 1
        a //= 10
    return count