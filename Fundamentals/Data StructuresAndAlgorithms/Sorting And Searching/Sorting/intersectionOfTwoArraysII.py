"""
-Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

#Timr complexity: O(nlogn)
#Space complexity: O(len1 or len2) in worst case
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []

    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1, nums2))