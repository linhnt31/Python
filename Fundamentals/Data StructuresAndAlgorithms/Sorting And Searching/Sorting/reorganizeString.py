"""
-Link: 
"""
def reorganize_string(s):
    count = [0] * 26
    for substr in s:
        count[ord(substr) - ord('a')] += 1
    ans = []

    for val in count:
        if len(s) % 2 == 0:
            if val > len(s) // 2:
                return ''
        else:
            if val > len(s) // 2 + 2:
                return ''
    
    for i in range(len(count)):
        if count[i] != 0:
            ans.append(chr(i + 97))
            count[i] -= 1
        for j in range(i + 1, len(count)):
            if count[j] != 0:
                ans.append(chr(j + 97))
                count[j] -= 1
    for i in range(len(count)):
        if count[i] != 0:
            ans.append(chr(i + 97))
    return ''.join(ans)

if __name__ == "__main__":
    s = 'aaab'
    print(reorganize_string(s))