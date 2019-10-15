"""
-Referrence: http://www.code-in-python.com/calculating-any-term-of-the-fibonacci-sequence-using-binets-formula/
"""
import math

def caculate(n):
    sqrt5 = math.sqrt(5)

    return int(((1 + sqrt5) ** n - (1 - sqrt5) ** n) // (2 ** n * sqrt5) )

if __name__ == "__main__":
    n = int(input('Enter a random number: '))
    print('nth of fibonaci: {}'.format(caculate(n)))