"""
-Link: https://app.codesignal.com/challenge/h7i7qTRoon4KSekYk
"""

def arraySumAdjacentDifference(a):

    res = 0
    for i in range(1, len(a)):
        res += abs(a[i] - a[i - 1])
    return res

