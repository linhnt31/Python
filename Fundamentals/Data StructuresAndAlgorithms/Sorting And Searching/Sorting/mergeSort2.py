import random
import time 
#Implement the mergeSort function without using the slice operator.
#Time complexity: O(n^2)
#Space complexity: O(n) to create 2 temp lists
def merge_sort2(alist):
    if len(alist) > 1:
        mid  = len(alist) // 2
        tmp1 = [0] * mid
        tmp2 = [0] * (len(alist) - mid )

        #Copy data to 2 sublists
        for i in range(len(tmp1)):
            tmp1[i] = alist[i]

        for j in range(len(tmp2)):
            tmp2[j] = alist[mid + j]

        merge_sort2(tmp1)
        merge_sort2(tmp2)

        i = j = k = 0
        while i < len(tmp1) and j < len(tmp2):
            if tmp1[i] < tmp2[j]:
                alist[k] = tmp1[i]
                i += 1
                k += 1
            else:
                alist[k] = tmp2[j]
                j += 1
                k += 1
        
        #Copy data from the rest of 2 lists
        while i < len(tmp1):
            alist[k] = tmp1[i]
            i += 1
            k += 1

        while j < len(tmp2):
            alist[k] = tmp2[j]
            j += 1
            k += 1

    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(100000)]
    begin = time.clock()
    print("List before sorting: ", alist)
    print("List after sorting: ", merge_sort2(alist))
    end = time.clock()
    print("Running time: ", (end - begin))