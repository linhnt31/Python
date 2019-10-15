"""
-Link: https://www.geeksforgeeks.org/coin-change-dp-7/
"""


#S[0...m-1] to get sum to N
def count_change(S, m , N):
    if N == 0: 
        return 1
    if N < 0: 
        return 0
    if m <= 0 and N >= 1: 
        return 0

    
    return count_change(S, m-1,N) + count_change(S, m, N - S[m-1])

if __name__ == "__main__":
    S = [1, 2, 3]
    print(count_change(S, len(S), 4))