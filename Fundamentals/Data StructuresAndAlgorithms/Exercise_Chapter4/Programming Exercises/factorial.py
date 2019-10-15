"""
Write a recursive function to compute the factorial of a number.
"""

def __factorial(n):
    if n == 0:
        return 1
    return n * __factorial(n-1)

if __name__ == "__main__":
    n = int(input())
    print(__factorial(n))