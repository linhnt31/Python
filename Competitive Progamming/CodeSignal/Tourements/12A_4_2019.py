"""
-Link: https://app.codesignal.com/tournaments/PzHcEzCi3Thdc7dCY
-Link: https://app.codesignal.com/tournaments/7Mob8zsiTiP7vaKxy
"""

#
def primeFactors(n):
    factors = []
    divisor = 2

    while n >= 2:
        if n % divisor != 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return factors

#
def evenDigitsOnly(n):
    while n > 0:
        tmp = n % 10
        if tmp % 2 != 0:
            return False
        n //= 10
    return True

#
def isCaseInsensitivePalindrome(inputString):

    inputString = inputString.lower()
    
    return inputString == inputString[::-1]

#
def mergeSort(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left + 1 == right:
            return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence

#
def kthDivisor(n, k):

    res = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    
    if k > len(res):
        return -1
    return res[k-1]

#
def shareAnApple(a, b):

    return a - 1 == b + 1