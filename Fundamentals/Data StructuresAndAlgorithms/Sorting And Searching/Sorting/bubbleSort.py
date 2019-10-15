from random import randint

#Time complexity: O(n^2)
#Space complexity: O(1)
def bubble_sort(alist):

    for _ in range(len(alist)):
        check_swapped = False
        for j in range(len(alist)-1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                check_swapped = True
        if check_swapped == False:
            break
    return alist

if __name__ == "__main__":
    
    alist = [randint(0, 100) for _ in range(8)]
    print('Before sorting : ', alist)
    print(bubble_sort(alist))