myTree = [ 'a', #root
    ['b', #left subtree
    ['d', [], []],
    ['e', [], []]],
    ['c', #right subtree
    ['f', [], []],
    []]
]

print(myTree)
print('Root', myTree[0])
print('Left subtree', myTree[1])
print('Right subtree', myTree[2])
print('Children: ', myTree[1][1], myTree[1][2])