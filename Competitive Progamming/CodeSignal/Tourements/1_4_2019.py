'''
- Link: https://app.codesignal.com/tournaments/EGb9c7rn8tjrciqPH
'''

#
def checkSameElementExistence(arr1, arr2):

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            return True
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            j += 1

    return False

#
def arrayCenter(a):

    n = len(a)
    suma = a[0]
    mina = a[0]
    for i in range(1, n):
        mina = min(mina, a[i])
        suma += a[i]

    b = []
    for i in range(n):
        if abs(n * a[i] - suma) < n * mina:
            b.append(a[i])

    return b

#
def largestNumber(n):
    return 10 ** n - 1

#
def strangeCode(s, e):
    res = []
    count = 0
    while s < e - 1:
        s += 1
        e -= 1
        if count % 2 == 0:
            res.append('a')
        else:
            res.append('b')
        count += 1
    return ''.join(res)
        

#
def maxSumSegments(inputArray):
    res = []

    for i in range(len(inputArray)):
        count = i + 1
        max_ = -float('inf')
        ind = 0
        for j in range(len(inputArray) - count + 1):
            if max_ < sum(inputArray[j : j + count]):
                max_ = sum(inputArray[j : j + count])
                ind = j
        res.append(ind)

    return res
