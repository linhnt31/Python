"""
-Link: https://app.codesignal.com/challenge/FZPHHfMMv5QZJuZYi
"""

def houseOfCats(legs):
    ans = []
    i = 0
    while (legs - 4*i) // 2 >= 0:
        ans.append((legs - 4*i) // 2)
        i += 1
    return sorted(ans)