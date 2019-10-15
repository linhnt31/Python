"""
-Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""

#Time complexity: O(n*n)
#Space complexity: O(n) to contain the result.
def countSmaller(nums):
    if len(nums) == 0:
        return [0]
    ans = []
    for i in range(len(nums)-1):
        count = 0
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        ans.append(count)
    ans.append(0)
    return ans

#Solution 2: Optimized- Using BST and mergeSort 
# not enough knowledge to solve this problem.
#Time complexity: 
#Space complexity:
def countSmaller2(nums):
    pass

if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    print('Result: ', countSmaller(nums))