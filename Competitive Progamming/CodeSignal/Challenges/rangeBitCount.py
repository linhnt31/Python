"""
-Link: https://app.codesignal.com/tournaments/APMX22un6jH82KwSx/A
"""
def rangeBitCount(a, b):
    res = 0

    for i in range(a, b + 1):
        tmp = i
        while tmp != 0:
            res += tmp & 1
            tmp = tmp >> 1
    return res


if __name__ == "__main__":
    a = 2
    b = 7

    print(rangeBitCount(a, b))