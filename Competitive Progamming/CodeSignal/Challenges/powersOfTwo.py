'''
- Link: https://app.codesignal.com/challenge/py5NYKrfAQ5qLe4SP
'''

#Solution 1: 
def powersOfTwo1(n):

    ans = []
    cur = 1
    while n > 0:
        if n % 2 == 1:
            ans.append(cur)
        n >>= 1
        cur <<= 1

    return ans

#Solution 2:
def powersOfTwo2(n):
    ans = []
    c = 1
    
    while n:
        if n % 2:
            ans.append(c)
        c *= 2
        n //= 2
    return ans
