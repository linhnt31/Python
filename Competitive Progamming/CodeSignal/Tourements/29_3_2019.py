'''
- Link: https://app.codesignal.com/tournaments/gbpM6k4xuPHe6kYoF
- Link: https://app.codesignal.com/tournaments/guHgeLnE92yd4WWer
'''

''' Contest 1 '''
#
def myMaxOfThree(a, b, c):
    if a > b:
        if a > c:
            return a
        return b
    if b > c:
        return b
    return c

#
def circleOfNumbers(n, firstNumber):
    return (n // 2 +firstNumber) % n

#
def sumUpDigits(inputString):
    res = 0
    for x in inputString:
        if x >= '0' and x <= '9':
            res += int(x)
    return res

#
def maxMultiple(divisor, bound):
    while bound >= 0:
        if bound % divisor == 0:
            return bound
        bound -= 1

''' Contest 2 '''
#
def numberOfEvenDigits(n):
    result = 0
    while n != 0:
        if n % 2 == 0:
            result += 1
        n /= 10
    return result

#
def countSumOfTwoRepresentations(n, l, r):

    count = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            if i + j == n:
                count += 1
    return count

#
def higherVersion(ver1, ver2):
    lst1 = ver1.split('.')
    lst2 = ver2.split('.')
    
    for i in range(len(lst1)):
        if int(lst1[i]) < int(lst2[i]):
            return False
        elif int(lst1[i]) > int(lst2[i]):
            return True
    return False

#
def zFunctionNaive(s):
    res = []
    
    for i in range(len(s)):
        count = 0
        tmp_ind = i
        for j in range(len(s)):
            if tmp_ind < len(s) and s[j] == s[tmp_ind]:
                count += 1
                tmp_ind += 1
            else:
                break
        res.append(count)
    return res