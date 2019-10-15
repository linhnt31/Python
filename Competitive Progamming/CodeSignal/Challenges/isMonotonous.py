"""
-Link: https://app.codesignal.com/challenge/Bbr2AGZQw2CHofuao
"""

def isMonotonous(a):

    if len(a) <= 1:
        return True
    elif len(a) == 2:
        return a[0] != a[1]
    
    tmp = a[1] - a[0]
    for i in range(2, len(a)):
        if tmp * (a[i] - a[i-1]) <= 0:
            return False
        tmp = a[i] - a[i-1]
    return True