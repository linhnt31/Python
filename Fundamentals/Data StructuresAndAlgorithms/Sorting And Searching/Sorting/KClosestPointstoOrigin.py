"""
-Link: https://leetcode.com/problems/k-closest-points-to-origin/
"""

#Time complexity: O()
#Space complexity: 
def kClosest(points, k):
    points.sort(key= lambda x : x[0] ** 2 + x[1] ** 2)
    return points[:k]

if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    print(kClosest(points, 1))