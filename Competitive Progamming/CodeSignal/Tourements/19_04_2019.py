"""
-Link: https://app.codesignal.com/tournaments/n8qAhcgHZLy37xtPp
"""

#
def zFunctionNaive(s):

    result = []

    for i in range(len(s)):
        result.append(0)
        for j in range(i, len(s)):
            if s[j] == s[result[i]]:
                result[i] += 1
            else:
                break

    return result

#
def reachNextLevel(experience, threshold, reward):
    experience += reward
    if experience >= threshold:
        return True
    return False

#
def oddNumbersBeforeZero(sequence):
    count = 0
    for x in sequence:
        if x == 0:
            break
        elif x % 2 != 0:
            count += 1
    return count

#
def computeDefiniteIntegral(l, r, p):

    res = 0
    tmp1, tmp2 = l, r
        
    for i in range(len(p)):
        res += p[i] * (tmp2-tmp1) / (i + 1)
        
        tmp1 *= l
        tmp2 *= r
    return res

#
def create2DArray(lengths):

    res = []
    for i in lengths:
        res.append([j for j in range(i)])
    return res