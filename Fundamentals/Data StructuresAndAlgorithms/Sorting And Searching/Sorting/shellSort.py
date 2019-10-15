import random

#Time complexity: It falls between O(n) and O(n 2 ). --> Can impove by changing the increment
#Space complexity: O(1)
def shell_sort(alist):
    gap = len(alist) // 2

    while gap > 0:
        for i in range(gap, len(alist)):
            current_value = alist[i]
            j = i

            while j >= gap and current_value < alist[j - gap]:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = current_value
        gap //= 2
    
    return alist


if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print("Before sorting: ", alist)
    print("After sorting: ", shell_sort(alist))