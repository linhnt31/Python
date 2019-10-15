# Using recursion: 

def fib1(n):
    if n <= 1: 
        return n
    return fib1(n - 1) + fib1(n - 2)

#Using dynamic progamming
#Time comlexity: O(n)
def fib2(n):
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

if __name__ == "__main__":
    while True:
        n = int(input('Enter a random value: '))
        print(f'res1 = {fib1(n)} ::: res2 = {fib2(n)}')
