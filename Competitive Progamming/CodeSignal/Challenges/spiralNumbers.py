"""
-Link: https://app.codesignal.com/challenge/JiFpoZHM4ogdn5xQc
"""

def spiralNumbers(n):
    ans =  [ [0]*n for i in range(n)]
    p=1;
    r=0;
    for i in range(n,0,-2):
        for a in range(0,i):
            ans[r][a+r]=p
            p+=1
        for b in range(r+1,i+r):
            ans[b][i-1+r]=p
            p+=1
        for c in range(i-2+r,r-1,-1):
            ans[i-1+r][c]=p
            p+=1
        for d in range(i-2+r,r,-1):
            ans[d][r]=p
            p+=1
        r+=1
    return ans
