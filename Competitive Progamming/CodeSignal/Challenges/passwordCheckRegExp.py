"""
- Link: https://app.codesignal.com/challenge/LpN6NK7cyQmzFukC5
"""

import string
def passwordCheckRegExp(inp):
    c1, c2, c3 = 0, 0, 0
    if len(inp) < 5:
        return False
    
    for x in inp:
        if 'A' <= x <= 'Z':
            c1 += 1
        elif 'a' <= x <= 'z':
            c2 += 1
        elif '0' <= x <= '9':
            c3 += 1
    return c1 >= 1 and c2 >= 1 and c3 >=1