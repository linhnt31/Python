"""
-Link: https://app.codesignal.com/tournaments/Y4aDivacwhEjNvfXB
"""

#
def areIsomorphic(array1, array2):

    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if len(array1[i]) != len(array2[i]):
            return False
    return True

#
def concatenationProcess(initialArray):

    while len(initialArray) > 1:
        minInd1 = 0
        minInd2 = len(initialArray) - 1

        for i in range(1, len(initialArray)):
            if len(initialArray[i]) < len(initialArray[minInd1]):
                minInd1 = i

        if minInd2 == minInd1:
            minInd2 -= 1

        for i in range(len(initialArray) - 2, -1, -1):
            if (len(initialArray[i]) < len(initialArray[minInd2])
            and i != minInd1):
                minInd2 = i

        initialArray.append(initialArray[minInd1] + initialArray[minInd2])
        initialArray = (initialArray[:max(minInd1, minInd2)] +
                        initialArray[max(minInd1, minInd2) + 1:])
        initialArray = (initialArray[:min(minInd1, minInd2)] +
                        initialArray[min(minInd1, minInd2) + 1:])

    return initialArray[0]

#
def fullName(first, last):

    return first + " " + last

#
def strangeCode(s, e):
    res = []
    count = 0
    
    while s < e - 1:
        if count % 2 == 0:
            res.append('a')
        else: 
            res.append('b')
        s += 1
        e -= 1
        count += 1
    return "".join(res)
