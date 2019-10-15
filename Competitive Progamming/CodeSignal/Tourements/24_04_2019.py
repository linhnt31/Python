"""
- Link: https://app.codesignal.com/tournaments/PncAc3SLLCKtEK27k
- Link: https://app.codesignal.com/tournaments/ApxYFasSxFwx3Y3hE
"""

#
def isAdult(age, adulthoodAge):
    if age >= adulthoodAge:
        answer = True
    if age < adulthoodAge:
        answer = False

    return answer

#
def countLineColorings(points, colors):
    result = colors
    for _ in range(1, points):
        result *= colors - 1
    return result

#
def squarePerimeter(n):

    return 4 * n

#
def makeArrayConsecutive2(statues):

    tmp = sorted(statues)
    return(max(tmp) - min(tmp) - len(statues) + 1)

#
def increaseNumberRoundness(n):

    while n % 10 == 0:
        n //= 10
    
    tmp = str(n)
    
    return '0' in tmp

#
def isInfiniteProcess(a, b):
    return a > b or (b - a) % 2 == 1

#
def commonCharacterCount(s1, s2):
    map1 = {}
    map2 = {}
    answer = 0

    for i in range(len(s1)):
        char = s1[i]
        if char in map1:
            map1[char] += 1
        else:
            map1[char] = 1

    for i in range(len(s2)):
        char = s2[i]
        if char in map2:
            map2[char] += 1
        else:
            map2[char] = 1

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        answer += min(map1.get(char, 0) , map2.get(char, 0))
    return answer

#
def lateRide(n):

    tmp = int(str(n // 60) + str(n % 60))
    res = 0
    while tmp > 0:
        res += tmp % 10
        tmp //= 10
        
    return res
#
def checkEqualFrequency(a):
    if len(a) == 1: return True
    map  = {}
    tmp = []
    for i in a:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
            
    for i in set(a):
        tmp.append(map.get(i))
    return len(set(tmp)) == 1
    
#