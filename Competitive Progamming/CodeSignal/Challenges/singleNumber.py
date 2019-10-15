"""
-Link: https://app.codesignal.com/interview-practice/task/APDXraJZYfPSYqQMJ/solutions
"""

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
