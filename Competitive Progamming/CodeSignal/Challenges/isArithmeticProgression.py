"""
-Link: https://app.codesignal.com/challenge/s4AfxmEgtJdA9ANJr
"""

def isArithmeticProgression(a):
    if len(a) < 2:
        return True
    tmp = a[1] - a[0]
    for i in range(2, len(a)):
        if a[i] - a[i-1] != tmp:
            return False
    return True
        