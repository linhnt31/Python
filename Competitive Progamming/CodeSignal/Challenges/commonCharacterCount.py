"""
-Link: https://app.codesignal.com/tournaments/ApxYFasSxFwx3Y3hE/B
"""

def _commonCharacterCount(s1, s2):
    map1, map2 = {}, {}
    res = 0

    for ch in s1:
        if ch in map1:
            map1[ch] += 1
        else:
            map1[ch] = 1

    for ch in s2:
        if ch in map2:
            map2[ch] += 1
        else:
            map2[ch] = 1
    
    for i in range(ord('a'), ord('z') + 1):
        ch = chr(i)
        res += min(map1.get(ch, 0), map2.get(ch, 0))
    return res

if __name__ == "__main__":
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    print(_commonCharacterCount(s1, s2))