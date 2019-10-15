"""
-Link: https://app.codesignal.com/challenge/sn4MqAwzXnDiGG9Nb
"""

def checkFactorial(n):

    i = 2
    while n % i == 0:
        n //= i
        i += 1
    return n == 1