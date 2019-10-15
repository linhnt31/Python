"""
-Link: https://app.codesignal.com/challenge/r3f8PoCN4YCn634an
"""

def isPermutation(n, inputArray):

    tmp = sorted(inputArray)
    
    if len(set(tmp)) < len(tmp):
        return False
    for x in tmp:
        if x not in range(1, n+1):
            return False
    return True