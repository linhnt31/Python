"""
-Link: https://app.codesignal.com/tournaments/tsYCA2DyCJrDoeCxQ
"""

#
def isIncreasingDigitsSequence(n):
    last = 10
    while n != 0:
        if n % 10 > last:
            return False
        last = n % 10
        n //= 10
    return True

#
def axisAlignedBoundingBox(x, y):

    minX = x[0]
    maxX = x[0]
    minY = y[0]
    maxY = y[0]

    for i in range(1, len(x)):
        minX = min(x[i], minX)
        maxX = max(x[i], maxX)
        minY = min(y[i], minY)
        maxY = max(y[i], maxY)

    return (maxX - minX) * (maxY - minY)

#
def reverseToSort(a):

    for i in range(len(a) - 1):
        for j in range(i + 2, len(a) + 1):
            tmp = a[i : j]
            if sorted(a) == a[:i] + tmp[::-1] + a[j:]:
                return len(set(a)) == len(a)
    return False

#
def fractionReducing(fraction):
    t = gcd(fraction[0], fraction[1])
    
    return [fraction[0] // t, fraction[1] // t]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#
def compareIntegers(a, b):

    if int(a) > int(b):
        return 'greater'
    elif int(a) == int(b):
        return 'equal'
    return 'less'