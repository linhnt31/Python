"""
-Link: https://app.codesignal.com/interview-practice/task/oJXTWuwEZiC6FTw3A/solutions
"""

# def climbingStairs(n):
#     f0, f1 = 1, 2
#     next_fi = None
#     if n == 1: return 1
#     elif n == 2: return 2
#     else:
#         for _ in range(3, n+ 1):
#             next_fi = f0 + f1
#             f0 = f1
#             f1 = next_fi
#     return next_fi
       
#Use dynamic progamming
def climbingStairs(n):
    
    if n <= 2: return n
    
    res = [0]*n
    res[0] = 1
    res[1] = 2
    
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[n-1]