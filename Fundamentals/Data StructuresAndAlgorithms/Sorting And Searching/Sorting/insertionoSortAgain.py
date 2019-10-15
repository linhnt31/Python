import random

#Always maintain a sublist sorted
def insertionSort_V2(alist):
    for i in range(1, len(alist)):
        j = i 
        current_value = alist[i]

        while j > 0 and alist[j - 1] > current_value:
            alist[j] = alist[j - 1]
            j -= 1
        
        alist[j] = current_value
    return alist

if __name__ == "__main__":
    alist = [random.randint(0, 100) for _ in range(8)]
    print('Before sorted: ', alist)
    print('After sorted: ', insertionSort_V2(alist))