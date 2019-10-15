"""
-Link: https://www.geeksforgeeks.org/ugly-numbers/
"""
#Method 1: Loop
#Time complexity: O(n^2)
#Space complexity: O(1)
def maxDivide(a, b):
    while a % b == 0:
        a //= b
    return a

def checkUgly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)

    return True if n == 1 else False

def getNthUgly(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if checkUgly(i):
            count += 1
    return i


#Method 2: Using Dynamic progamming
#Time comlexity: O(n)
#Space complexity: O(n)
def getNthUglyDynamic(n):
    if n <= 0:
        return "You must enter n > 0 !!!"
    #To store ugly numbers
    ugly = [0] * n 
    
    #Initialize first ugly number
    ugly[0] = 1

    #i2, i3, i5 will indicate indices for 2, 3, 5 respectively
    i2 = i3 = i5 = 0

    #set initial multiple values
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n] 
    for i in range(1, n):
        # choose the min value of all available multiples
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # increment the value of index accordingly
        if ugly[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        
        if ugly[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        
        if ugly[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    return ugly[-1]


#main
if __name__ == "__main__":
    while True:
        n = int(input('Enter a random number: '))
        print(getNthUgly(n))
        print(getNthUglyDynamic(n))