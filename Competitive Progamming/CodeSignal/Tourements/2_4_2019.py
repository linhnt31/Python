'''
- Link: https://app.codesignal.com/tournaments/cjGjGbCZYTqRYLwNK
'''

#
def sumOfMultiples(n, k):

    tmp = k
    count = 0
    while tmp <= n:
        if tmp % k == 0:
            count += tmp
        tmp += 1
    return count

# no optimization
def champernowneDigit(n):
    tmp = [str(i) for i in range(1, 100)]
    str_  = "".join(tmp)
    
    return int(str_[n - 1])

#
def magicalWell(a, b, n):
    sum_ = 0
    while n > 0:
        sum_ += a * b
        a += 1
        b += 1
        n -= 1
        
    return sum_
