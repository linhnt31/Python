import random

#Time complexity: O(nlogn)
#Auxillary complexity: 
#Space complexity: 
def partition(alist, begin, last):
    pivot = alist[last]
    pIndex = begin

    for i in range(begin, last + 1):
        if alist[i] < pivot:
            alist[i], alist[pIndex] = alist[pIndex], alist[i]
            pIndex += 1
    alist[pIndex], alist[last] = alist[last], alist[pIndex]
    return pIndex

def quickSort_V2(alist, left, right):
    if left < right:
        pIndex = partition(alist, left, right)
        quickSort_V2(alist, left, pIndex - 1)
        quickSort_V2(alist, pIndex + 1, right)

if __name__ == "__main__":
    alist = [1, 8, 5, 2, 4]
    print('Before sorted: ', alist)
    print('After sorted: ')
    quickSort_V2(alist, 0, len(alist)-1)
    print([i for i in alist])
