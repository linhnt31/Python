"""
-Link: https://app.codesignal.com/interview-practice/task/XBWN6DYRqPrKdMZs8
"""

#Dynamic Progamming
#Time complexity: O(n)
#Space complexity: O(n)

def houseRobber(nums):

    length = len(nums)
    if length == 0:
        return 0
    elif length == 1:
        return nums[0]
  
    max_ = [0] * len(nums)
    max_[0] = nums[0]
    max_[1] = max(nums[0], nums[1])
    
    for i in range(2, length):
        max_[i] = max(max_[i-2] + nums[i], max_[i-1])
    return max_[length - 1]