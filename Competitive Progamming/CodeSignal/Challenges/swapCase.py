"""
-Link: https://app.codesignal.com/challenge/NCuzDQJSWeAicpQKX
"""

def swapCase(text):
    res = ''
    for v in text:
        if 'a' <= v <= 'z':
            res +=  v.upper()
        else:
            res += v.lower()
    return res