"""
-Link: https://leetcode.com/problems/intersection-of-two-arrays/
"""

#Time complexity: O(nlogn) n is value which is less than other value
def intersection(num1, num2):
    i = j = 0
    num1.sort()
    num2.sort()
    ans = []
    while i < len(num1) and j < len(num2):
        if num1[i] == num2[j] and num1[i] not in ans:
            ans.append(num1[i])
        elif num1[i] > num2[j]:
            j += 1
        else:
            i += 1
    return ans

#Time complexity: O(n + m)
#Space complexity: O(n + m) in the worst case

def optimize(num1, num2):
    set1 = set(num1)
    set2 = set(num2)

    if len(set1) < len(set2):
        return [x for x in set1 if x in set2]
    return [x for x in set2 if x in set1]

if __name__ == "__main__":
    num1 = [4,9,5]
    num2 = [9,4,9,8,4]
    print(intersection(num1, num2))
    print(optimize(num1, num2))

