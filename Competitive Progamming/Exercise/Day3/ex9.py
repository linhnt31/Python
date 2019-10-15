'''
BT9
Viết chương trình để flatten list sau: [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
Kết quả cần đạt được: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

lst = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [[[[[6]]]]], [10]]
res = []
while lst:
    sub_lst = lst.pop()
    '''
    import pdb      #Convenient for debug
    pdb.set_trace()
    '''
    if isinstance(sub_lst, list): # recommend using isinstance() than using typy()
    # if type(sub_lst) == list:
        lst += sub_lst
        # print(lst)
    else:
        # print(sub_lst)
        res.append(sub_lst)


# res.sort()
print(res[::-1])


#Fix homework
