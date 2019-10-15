"""
-Link: https://app.codesignal.com/tournaments/CpqbG4S82fhHAJz5s
-Link: https://app.codesignal.com/tournaments/MBqmnXSctTSLkeFCv
"""

#
def isSumOfConsecutive(n):
    for start in range(1, n):
        number = n
        subtrahend = start
        while number > 0:
            number -= subtrahend
            subtrahend += 1
        if number == 0:
            return True
    return False

#
def getMonthName(mo):
    mo -= 1
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if mo >= 0 and mo < len(months):
        return months[mo]
    else:
        return "invalid month"

#
def firstMultiple2(divisors, start):

    while True:
        for x in divisors:
            if start % x == 0:
                return start
        start += 1

#
def depositProfit(deposit, rate, threshold):
    res = 0
    
    while deposit < threshold:
        deposit += (deposit * rate) / 100
        res += 1
    return res

#
def numberOfEvenDigits(n):

    res = 0
    while n > 0:
        tmp = n % 10
        if tmp % 2 == 0:
            res += 1
        n //= 10
    return res

#
def rightTriangle(sides):

    def sqr(value):
        return value * value

    sides.sort()
    if sqr(sides[0]) + sqr(sides[1]) == sqr(sides[2]):
        return True
    return False


#
def triangleExistence(sides):

    sides = sorted(sides)

    if sides[0] + sides[1] > sides[2]:
        return True
    return False

#
def integerToStringOfFixedWidth(number, width):

    tmp = str(number)
    if len(tmp) <= width:
        return '0' * (width - len(tmp)) + tmp
    
    return tmp[len(tmp)-width:]

#
def isAdult(age, adulthoodAge):

    return age >= adulthoodAge
