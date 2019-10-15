import random

#Time complexity: O(n^2)
#Space complexity: O(1)
def selection_sort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        
        #Swap the found minimum element with i'st element
        alist[min_index], alist[i] = alist[i], alist[min_index]

    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print("Before sorting: ", alist)
    print(selection_sort(alist))