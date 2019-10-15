'''
-Link : https://app.codesignal.com/tournaments/ye9ht6YQ6dwgPeiSi
'''

#
def mySqrtNaive(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

#
def reachNextLevel(experience, threshold, reward):
    experience += reward
    if experience >= threshold:
        return True
    return False


#
def makeArrayConsecutive(sequence):
    res = []
    sequence.sort()
    
    for i in range(min(sequence), max(sequence) + 1):
        if i not in sequence:
            res.append(i)
    return res


#
def parallelLines(line1, line2):
    return line1[0] * line2[1] == line1[1]*line2[0]


#
def fullName(first, last):
    return first + " " + last
