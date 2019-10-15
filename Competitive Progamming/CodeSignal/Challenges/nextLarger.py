"""
- Link: https://app.codesignal.com/interview-practice/task/MdHZFgZFERPPagfdD
"""

# Solution 1:
#Time complexity: O(n^2)

def nextLarger1(a):

    if len(a) == 1:
        return [-1]
    
    res = []
    
    for i in range(0, len(a) - 1):
        added = False
        for j in range(i + 1, len(a)):
            if a[j] > a[i]:
                res.append(a[j])
                added = True
                break
        if added == False:
            res.append(-1)
    res.append(-1)
    return res

#Solution 2: 
#Time complexity: O(n)

def nextLarger2(a):

    stack = []
    ans = []
    
    for x in a[::-1]:
        while stack and x > stack[-1]:
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(x)
    return ans[::-1]
