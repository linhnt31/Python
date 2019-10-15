"""
-Link: https://app.codesignal.com/challenge/JgRCNpe2zbiqGsp8b
"""

def improperFractionToMixed(a):
    
    m, n = a[0], a[1]
    return [m // n, m % n, n]