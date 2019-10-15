'''
- Link: https://app.codesignal.com/challenge/mrAXkgwfH5a9HCyuL
'''

def differentValues(a, d):

    res = -1

    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            tmp = abs(a[i] - a[j])
            if tmp <= d and res < tmp:
                res = tmp 
    return res