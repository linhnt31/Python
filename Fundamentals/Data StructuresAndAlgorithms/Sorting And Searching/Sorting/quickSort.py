import random

#Time complexity: O(nlogn)
#Space complexity: O(1)
def partition(alist, start, end):
    pivot  = alist[end]
    pivot_index = start

    for i in range(start, end):
        if alist[i] <= pivot:
            alist[i], alist[pivot_index] = alist[pivot_index], alist[i]
            pivot_index += 1
    alist[pivot_index], alist[end] = alist[end], alist[pivot_index]
    return pivot_index

def quick_sort(alist, start , end):
    if start < end:
        pivot_index = partition(alist, start, end)
        quick_sort(alist, start, pivot_index - 1)
        quick_sort(alist, pivot_index + 1, end)
    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print("Before sorting: ", alist)
    print("After sorting: ",quick_sort(alist, 0, len(alist) - 1))