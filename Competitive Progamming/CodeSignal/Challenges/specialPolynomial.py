"""
-Link: https://app.codesignal.com/challenge/9EYdtrq7ZytJy6Fy4
"""

def specialPolynomial(x, n):
    res = 1
    i = 1
    while res <= n:
        res += x ** i
        i += 1
    return i - 2

