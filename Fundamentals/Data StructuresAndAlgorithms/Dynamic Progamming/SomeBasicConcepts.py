""" Tabulation method: Bottom up """

def factorial(n):
    dp = [-1] * (n + 1)
    #base case
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]

""" Memoization Method: Top down """

def factorial2(n):
    dp = [-1] * (n + 1)
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    return  n * factorial2(n - 1)


if __name__ == "__main__":
    print(f'{factorial(4)}')
    print(f'{factorial2(4)}')

