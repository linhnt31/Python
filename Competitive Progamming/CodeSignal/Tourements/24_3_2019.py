'''
- Link: https://app.codesignal.com/tournaments/22iTYRRwKp9vaK4Lo
- Link: https://app.codesignal.com/tournaments/mSJ4kmmSQXy5o765X
'''

#
def angleType(measure):

    if measure < 90:
        return 'acute'

    if measure == 90:
        return 'right'

    if measure < 180:
        return 'obtuse'

    return 'straight'

#
def cyclicSequence(sequence):

    found = False
    st = -1
    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            return False
        if sequence[i - 1] > sequence[i]:
            if found:
                return False
            found = True
            st = i

    return st == -1 or sequence[0] > sequence[-1]

#
def magicalWell(a, b, n):
    sum_ = 0
    while n > 0:
        sum_ += a * b 
        a += 1
        b += 1
        n -= 1
    return sum_

#
def higherVersion(ver1, ver2):
    a = ver1.split('.')
    b = ver2.split('.')
    
    if len(a) != len(b):
        return False
    check = False
    for i in range(len(a)):
        if (int) (a[i]) < (int)(b[i]):
            break 
        elif (int) (a[i]) > (int)(b[i]):
            check = True
            break
    return check

#
def minMaxDifference(inputArray):

    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMinimum]:
            indexOfMaximum = i
    return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]

#
def knapsackLight2(weight1, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return 'both'
    if min(weight1, weight2) > maxW:
        return 'none'
    if max(weight1, weight2) <= maxW:
        return 'either'
    if weight1 <= maxW:
        return 'first'
    return 'second'

#
def orthogonalLines(line1, line2):
    return line1[0] * line2[0] + line1[1] * line2[1] == 0

#
def digitDegree(n):
    if n < 10:
        return 0
    
    return 1 + digitDegree(sum_(n))

def sum_(n):
    res = 0
    while(n > 0):
        res += n % 10
        n //= 10
    return res

#
def isDivisibleBy6(inputString):
    res = []
    
    for i in range(0, 10):
        tmp = inputString.replace('*', str(i))
        if int(tmp) % 6 == 0:
            res.append(tmp)
    return res
