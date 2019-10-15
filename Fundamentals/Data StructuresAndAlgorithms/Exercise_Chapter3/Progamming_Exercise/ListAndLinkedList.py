lst = [1, 2, 3]
print(id(lst[0]))
print(id(lst))

lst.append(4)
print(id(lst))

print(id(lst[0]), id(lst[1]), id(lst[2]), id(lst[3]))


"""  Answer 

*Approach: List in python has array implementation -
what this means is elements of list are stored in contiguous memory locations. So operations like index(), search()(binary search - 
if data is sorted), sort() can be really efficient. 
 
*Cons here is when the list is full and we need to add more data to it,
python has to copy the old list to a bigger contiguous space, similarly when we have removed a lot of elements from the list we need to resize() it to smaller size 
-this again requires copy to smaller contiguous memory locations.

"""