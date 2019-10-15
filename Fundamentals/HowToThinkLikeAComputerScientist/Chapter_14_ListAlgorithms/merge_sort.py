'''
Suppose we have two sorted lists. 
Devise an algorithm to merge them together into a single sorted list.
'''
import time

def merge(lst1, lst2):
    #initialize sorted list after merge
    res = []
    # indexs of two halves
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    # append rest of two lists
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst2):
        res.append(lst2[j])
        j += 1

    return res

lst1 = [14, 15, 16, 17, 18, 19, 20, 22, 330]
lst2 = [1, 2, 3, 4, 6, 10, 11, 12]

t0 = time.clock()
res = merge(lst1, lst2)
print('After merge sort: ', res)
t1 = time.clock()
print('Running time by using merge sort: ', (t1 - t0))

t2 = time.clock()
res1 = (lst1 + lst2).sort()
t3 = time.clock()
print('Running time by using append 2 lists: ', (t3 - t2))
print('{}'.format((t1 - t0) / (t3 - t2)))