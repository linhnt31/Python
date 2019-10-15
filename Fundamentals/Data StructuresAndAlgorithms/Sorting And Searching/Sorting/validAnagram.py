"""
-Link: https://leetcode.com/problems/valid-anagram/
"""

#Time comlexity: O(n)
#Space complexity: O(1)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s1 = [0] * 26
    s2 = [0] * 26

    for i in range(len(s)):
        s1[ord(s[i]) - ord('a')] += 1
        s2[ord(t[i]) - ord('a')] += 1
    
    for i in range(26):
        if s1[i] != s2[i]:
            return False
    return True


def optimize(s, t):
    if len(s) != len(t):
        return False
    
    counter = [0] * 26
    for i in range(len(s)):
        counter[ord(s[i]) - ord('a')] += 1
        counter[ord(t[i]) - ord('a')] -= 1
    
    for i in range(26):
        if counter[i] != 0:
            return False
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    print(optimize(s, t))