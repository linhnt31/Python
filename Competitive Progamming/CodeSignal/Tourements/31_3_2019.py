'''
- Link: https://app.codesignal.com/tournaments/SdWp7XZ8LCY2Ch9bd
'''

#
def absoluteValuesSumMinimization(a):

    indexOfMinimum = -1
    minimalSum = float('inf')

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += a[j] - a[i]
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]

#
def lrSegmentNumber(l, r):
    result = 0
    while l <= r:
        result = result * 10 + l
        l += 1
    return result

#
def isPermutation(n, inputArray):
    for i in range(1, n + 1):
        if i not in inputArray:
            return False
    return True

#
def knapsackLight2(weight1, weight2, maxW):
    if weight1 <= maxW and weight2 > maxW:
        return 'first'
    elif weight2 <= maxW and weight1 > maxW:
        return 'second'
    elif weight1 + weight2 <= maxW:
        return 'both'
    elif weight1 <= maxW and weight2 <= maxW:
        return 'either'
    return 'none'

#
from itertools import permutations

def numberMinimization(n, d):
    n = int(n)
    def neighbors(n):
        for cand in permutations(str(n)):
            x = int("".join(cand))
            yield x
            if x % d: continue
            yield int(x/d)
    
    seen = set()
    stack = [n]
    ct = 0
    while stack:
        ct += 1
        node = stack.pop()
        for nei in neighbors(node):
            if nei not in seen:
                seen.add(nei)
                stack.append(nei)
        if ct > 10000: return min(seen)
    return min(seen)