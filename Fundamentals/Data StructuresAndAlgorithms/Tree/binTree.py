def binary_tree(r):
    return [r, [], []]

def insert_left(root, newBranch):
    left_children = root.pop(1)

    if len(left_children) > 1:
        root.insert(1,[newBranch, left_children, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insert_right(root, newBranch):
    right_children = root.pop(2)
    
    if len(right_children) > 1: 
        root.insert(2, [newBranch, [], right_children])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, newValue):
    root[0] = newValue

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


def buildTree(root):
    pass


if __name__ == "__main__":
    # root = binary_tree(3)
    # insert_left(root, 4)
    # insert_left(root, 5)
    # insert_right(root, 6)
    # insert_right(root, 7)
    # left_chid = get_left_child(root)
    # print(left_chid)
    # print(get_right_child(get_right_child(root)))
    pass