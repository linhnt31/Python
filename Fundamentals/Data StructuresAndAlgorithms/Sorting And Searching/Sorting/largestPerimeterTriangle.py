"""
-Link: https://leetcode.com/problems/largest-perimeter-triangle/
"""

#Time complexity: O(nlogn)
#Space complexity: O(1)
def largestPerimeter(a):
    ans = - float('inf')
    a.sort(reverse= True)

    if len(a) < 3:
        return 0

    for i in range(0, len(a) - 2):
        if sum(a[i : i + 3]) > ans and checkTrigale(a[i], a[i + 1], a[i + 2]):
            ans = sum(a[i : i + 3])
    return ans


def checkTrigale(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def optimize(a):
    a.sort(reverse= True)
    if len(a) < 3:
        return 0
    
    for i in range(0, len(a) - 2):
        if a[i + 2] + a[i + 1] > a[i]:
            return a[i + 2] + a[i + 1] + a[i]
    return 0

if __name__ == "__main__":
    a = [3,2,3,4]
    print(largestPerimeter(a))
    print(optimize(a))