""" Link: https://app.codesignal.com/tournaments/3BKWRDc77x35Jd27s/D/solutions """


def pagesNumbering(n):
    res = 0
    c = 0
    m = n
    while m != 0: 
        c += 1
        m //= 10
    for i in range(c, 0 ,-1):
        tmp = 10 ** (i - 1)
        res += (n - tmp + 1) * i
        n = 10 ** (i - 1) - 1
    return res 
