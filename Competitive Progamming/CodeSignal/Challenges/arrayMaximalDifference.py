"""
-Link: https://app.codesignal.com/challenge/QgFzbcamhfiRLABDo
"""

def arrayMaximalDifference(a):

    max_ = -float('inf')
    
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            tmp = abs(a[j] - a[i])
            if tmp > max_:
                max_ = tmp
    return max_