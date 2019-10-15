"""
-Link: https://app.codesignal.com/challenge/ikrZ4ujnBmJoH5yG3
"""

def kthDigit(n, k):
    tmp = str(n)
    if k > len(tmp) or k < 1:
        return -1
    return int(tmp[k-1])
