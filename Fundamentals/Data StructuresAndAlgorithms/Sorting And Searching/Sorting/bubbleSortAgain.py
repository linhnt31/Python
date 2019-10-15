import random

def bubbleSort_V2(alist):
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):

            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print('Before sorted: ', alist)
    print('After sorted: ', bubbleSort_V2(alist))
