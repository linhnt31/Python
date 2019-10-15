"""
-Link: https://app.codesignal.com/tournaments/z9hmKQCz5ieTHsfwJ
"""

#def twoArraysNthElement(array1, array2, n):

    def lowerBound(array, elem):
        l = -1
        r = len(array)
        while l + 1 < r:
            mid = (l + r) // 2
            if array[mid] <= elem:
                l = mid
            else:
                r = mid
        return l

    l = -1
    r = len(array1)

    while l + 1 < r:
        mid = (l + r) // 2
        pos = lowerBound(array2, array1[mid])

        if mid + pos + 1 <= n:
            l = mid
        else:
            r = mid

    if l > -1 and l + lowerBound(array2, array1[l]) + 1 == n:
        return array1[l]
    return twoArraysNthElement(array2, array1, n)

#
def maxDigit(n):

    result = 0
    while n > 0:
        result = max(result, n % 10)
        n = n // 10

    return result

#
def mySubstring(inputString, l, r):

    return inputString[l:r+1]
#
def longestWord(text):
    s = re.split('[^a-zA-Z]',text)
    return max(s,key=len)
#
def arraySumAdjacentDifference(a):

    ans = 0
    for i in range(len(a)-1):
        ans += abs(a[i] - a[i+1])
    return ans