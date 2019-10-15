"""
-Link: https://app.codesignal.com/challenge/TerQ5PCqqCRaDYEiM
"""

def summaryProficiency(a, n, m):

    res = 0
    i = 0
    while n > 0:
        if a[i] >= m:
            res += a[i]
            n -= 1
        i += 1
    return res