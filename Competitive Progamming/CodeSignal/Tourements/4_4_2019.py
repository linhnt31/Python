'''
- Link: https://app.codesignal.com/tournaments/7AsRsC8CDgGBWbMaq
'''

#
def differentValuesInMultiplicationTable2(n, m):
    found = [False] * (n * m + 1)
    result = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            found[i * j] = True

    for value in range(1, n * n + 1):
        if found[value]:
            result += 1

    return result

#
def digitCharactersSum(ch1, ch2):
    x1 = ord(ch1) - 48
    x2 = ord(ch2) - ord('0')
    if x1 + x2 < 10:
        return chr(ord('0') + x1 + x2)
    else:
        return '1' + chr(ord('0') + (x1 + x2) % 10)

#
def isTandemRepeat(inputString):
    len_  = len(inputString)
    if len_ % 2 == 0:
        return inputString[:len_ // 2] == inputString[len_ // 2:]
    return False

#
def largestNumber(n):
    return 10 ** n - 1

#
def permutationShift(permutation):
    #O(n)
#     index_of_element = []
#     count = 0
#     for e in permutation:
#         index_of_element.append(permutation.index(e))
    
#     res = [permutation[i] - index_of_element[i] for i in range(len(permutation))]
    
#     return max(res) - min(res)
    
    tmp = [e - i for i, e in enumerate(permutation)]
    
    return max(tmp) - min(tmp)