'''
- Link: https://app.codesignal.com/challenge/LX9DdHwEsfgRs5SQ7
'''

def arrayCenter(a):
    min_ = min(a)
    avg = sum(a) / len(a)
    res = []
    
    for element in a:
        if abs(element - avg) < min_:
            res.append(element)
    return res
