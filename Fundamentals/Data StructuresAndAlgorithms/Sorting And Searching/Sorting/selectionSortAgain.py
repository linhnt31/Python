import random

def selectioSort_V2(alist):
    if len(alist) < 2:
        return alist
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[min_index] >= alist[j]:
                min_index = j
        #swap 2 elements acording to order
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print('Before sorted: ', alist)
    print('After sorted: ', selectioSort_V2(alist))