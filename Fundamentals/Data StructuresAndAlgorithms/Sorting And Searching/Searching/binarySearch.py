#Time complexity: O(logn)
#Space complexity: O(1)

def binary_search1(alist, item)->bool:
    left = 0
    right = len(alist) - 1
    mid = (left + right) // 2

    #base case
    if left > right:
        return False

    elif alist[mid] == item:
        return True

    elif alist[mid] > item:
        return binary_search1(alist[:mid], item)

    else:
        return binary_search1(alist[mid + 1:], item)


def binary_search2(alist, item):
    left = 0 
    right = len(alist) - 1
    found = False 

    while left <= right and not found:
        mid = (left + right) // 2

        if alist[mid] == item:
            found = True
        
        elif alist[mid] < item:
            left = mid + 1

        else:
            right = mid - 1

    return found


if __name__ == "__main__":
    alist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 66]
    item = int(input('Enter a value you want to find: '))
    print(binary_search1(alist, item))
    print(binary_search2(alist, item))