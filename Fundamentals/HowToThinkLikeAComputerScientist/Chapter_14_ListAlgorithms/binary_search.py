import random

#list is ordered
#Implementing binary search by recursion
#Time complexity: O(logn)
def search_binary(lst, left, right, key):
    mid = left + (right - left) // 2

    if lst[mid] == key:
        return mid
    elif lst[mid] > key:
        return search_binary(lst, left, mid - 1, key)
    
    return search_binary(lst, mid + 1, right, key)

lst = [1, 3, 6, 9, 12, 20]
print('My list: ', lst)
key = int(input('Enter a key: '))
print('{} appears at {}'.format(key, search_binary(lst, 0, len(lst)- 1, key)))