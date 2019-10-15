"""
-Link: https://leetcode.com/problems/sort-array-by-parity-ii/
"""

#Time complexity: O(n**2)
def sortArrayByParityII(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if i % 2 == 0 and a[i] % 2 != 0:
                if a[j] % 2 == 0:
                    a[i], a[j] = a[j], a[i]
            if i % 2 != 0 and a[i] % 2 == 0:
                if a[j] % 2 != 0:
                    a[i], a[j] = a[j], a[i]
    return a

#Timecomplexity: O(n)
#Space complexity: O(n) ---> fixed
def optimize1(a):
    size = len(a)
    ans = [None] * size

    indexEven, indexOdd = 0, 1
    for k, v in enumerate(a):
        if v % 2 == 0:
            ans[indexEven] = v
            indexEven += 2
        else:
            ans[indexOdd] = v
            indexOdd += 2
    return ans

    #The below code can implement by slicing operator
    # ans[::2] = (x for x in a if x % 2 == 0)
    # ans[1::2] = (x for x in a if x % 2 != 0)

#Time complexity: O(n)
#Space complexity: O(1)
def optimize2(a):
    j = 1
    for i in range(0, len(a), 2):
        if a[i] % 2 == 1:
            while a[j] % 2 == 1:
                j += 2
            
            a[i], a[j] = a[j], a[i]
    return a


if __name__ == "__main__":
    a = [4, 2, 5, 7, 8, 15]
    print(a)
    print(sortArrayByParityII(a))
    print(optimize1(a))
    print(optimize2(a))