import random

def merge(alist, left,mid, right):
    size1 = (mid - left + 1)
    size2 = right - mid
    tmp1 = [0] * size1
    tmp2 = [0] * size2

    #Copy data from alist to 2 sublists 
    for i in range(0, size1):
        tmp1[i] = alist[left + i]
    for j in range(0, size2):
        tmp2[j] = alist[mid + j + 1]

    i = j = 0
    k = left

    #Meger 2 sublists
    while i < size1 and j < size2:
        if tmp1[i] <= tmp2[j]:
            alist[k] = tmp1[i]
            i += 1
        else:
            alist[k] = tmp2[j]
            j += 1
        k += 1
    
    #Adding the rest of 2 sublists
    while i < size1:
        alist[k] = tmp1[i]
        i += 1
        k += 1
    
    while j < size2:
        alist[k] = tmp2[j]
        j += 1
        k += 1

def mergeSort_V2(alist, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort_V2(alist, left, mid)
        mergeSort_V2(alist, mid + 1, right)
        merge(alist, left, mid, right)


if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print('Before sorted: ', alist)
    print('After sorted: ')
    mergeSort_V2(alist, 0, len(alist) - 1)
    print(alist)
