"""
-Link: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""
import time


#Method 1: Recursion
#Time complexity: exponential
#Space complexity: O(n) if we consider the function call stack size, otherwise O(1).

def NthFiboRecursive(n):
    if n <= 1:
        return n
    return NthFiboRecursive(n - 1) + NthFiboRecursive(n - 2)

#Method 2: Dynamic progamming
#Time complexity: O(n)
#Space complexity: O(1)

def NthFiboDynamic(n):
    f0, f1 = 0, 1
    next_fibo = None

    if n == 0: return 0
    if n == 1: return 1
    
    for _ in range(2, n + 1):
        next_fibo = f0 + f1
        f0 = f1 
        f1 = next_fibo

    return next_fibo

if __name__ == "__main__":
    while True:
        n = int(input('Enter a random number: '))
        # begin1 = time.clock()
        # print(f'Nth is {NthFiboRecursive(n)}')
        # end1 = time.clock()
        # print(f'Time of recursion is {end1 - begin1}')
        # print('-------------------------')

        begin2 = time.clock()
        print(f'Nth is {NthFiboDynamic(n)}')
        end2 = time.clock()
        print(f'Time of dynamic is {end2 - begin2}')
        print('=====================================')