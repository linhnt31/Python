import random


#Time complexity: O(nlogn)
#Space complexity: O(n)
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2

        first_half = alist[:mid]  #Divide the list elements 
        second_half = alist[mid:] # into 2 halves

        merge_sort(first_half) #Sorting the first half
        merge_sort(second_half) #Sorting the second half

        i = j = k = 0

        #Copy data to temp lists first_half and second_half
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                alist[k] = first_half[i]
                i += 1
            else:
                alist[k] = second_half[j]
                j += 1
            k += 1

        #Checking if any element was left
        while i < len(first_half):
            alist[k] = first_half[i]
            i += 1
            k += 1
        
        while j < len(second_half):
            alist[k] = second_half[j]
            j += 1
            k += 1

    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print("List before sorting: ", alist)
    print("List after sorting: ", merge_sort(alist))