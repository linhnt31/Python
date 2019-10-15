L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]

set_of_l1 = set(L1)
set_of_l2 = set(L2)
#elements in both L1 and L2
print(set_of_l1 & set_of_l2)  #Result: {3, 4, 5, 6}

#elements only in L1
print(set_of_l1.difference(set_of_l2))  #Result: {1, 2}

#elements only in L2
print(set_of_l2.difference(set_of_l1)) #Result: {8, 9, 10, 7}

#not in both L1 or L2
print(set_of_l1 ^ set_of_l2)