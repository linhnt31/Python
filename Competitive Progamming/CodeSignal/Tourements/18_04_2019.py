"""
-Link: https://app.codesignal.com/tournaments/TBvuWWoyrhLB57Gax
"""

#
def ball_distribution(colors, ballsPerColor, boxsize):
    res = 0
    capacity = boxsize
    current_box = 0

    for _ in range(colors):
        start_box = current_box
        for _ in range(ballsPerColor):
            capacity -= 1
            if capacity == 0:
                capacity = boxsize
                current_box += 1

        if (start_box < current_box and capacity < boxsize):
            res += 1
            
    return res

#
def sequenceElement(a, n):

    MOD = 10**5
    seq = []
    for i in range(5):
        seq.append(a[i])

    lastFive = (a[0] * 10**4 + a[1] * 10**3 +
                a[2] * 10**2 + a[3] * 10 + a[4])
    was = {}
    was[lastFive] = 4

    i = 5
    while True:
        seq.append((seq[i - 1] + seq[i - 2] +
                    seq[i - 3] + seq[i - 4] + seq[i - 5]) % 10)
        lastFive = (lastFive * 10 + seq[i]) % MOD
        if lastFive in was:
            last = was[lastFive]
            return seq[n % (i - last)]
        else:
            was[lastFive] = i
        i += 1

#
def myConcat(strings, separator):

    res = []
    for ch in strings:
        res.append(ch+ separator)
    return "".join(res)

#
def returnLocalValue():

    return "local value"

#
def lastDigitRegExp(inputString):

    for ch in inputString[::-1]:
        if '0' <= ch <= '9':
            return ch
        