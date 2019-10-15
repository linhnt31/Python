'''
- Link: https://app.codesignal.com/challenge/cksc3cndoKiuZhe6Y
'''

def maxMultiple(divisor, bound):
    n = bound
    while n > 0:
        if n % divisor == 0:
            return n 
        n -= 1