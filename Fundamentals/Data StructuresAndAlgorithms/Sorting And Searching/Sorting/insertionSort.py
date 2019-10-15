import random
import time 

#Time complexity: O(n^2)
#Space complexity: O(1)
def insertion_sort(alist):
    for i in range(1, len(alist)):
        j = i 
        current_value = alist[i]

        while j >= 0 and alist[j-1] >= current_value:
            alist[j] = alist[j-1]
            j -= 1
        
        alist[j] = current_value
    return alist

if __name__ == "__main__":
    
    alist = [random.randint(0, 100) for _ in range(10000)]
    begin = time.clock()
    print("Before sorting: ", alist)
    print(insertion_sort(alist))
    end = time.clock()
    print("Running time: ",(end - begin))