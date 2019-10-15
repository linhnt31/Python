"""
-Link: https://app.codesignal.com/challenge/jHTZZohrRqu5ymqWJ
"""

def angleType(a):

    if a < 90:
        return "acute"
    elif a == 90:
        return "right"
    elif 90 < a < 180:
        return "obtuse"
    return "straight"