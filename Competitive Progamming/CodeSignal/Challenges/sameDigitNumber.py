'''
-Link : https://app.codesignal.com/challenge/hPDnpTSkih3XYMnZF
'''

def sameDigitNumber(n):
    if n < 10:
        return True
    res = []
    while n > 0:
        res.append(n % 10)
        n //=10
    return len(set(res)) == 1
