"""
- Referrence: https://www.geeksforgeeks.org/doubly-linked-list/
"""


class _Node:
    """ class Node of a DLL """
    def __init__(self, item):
        self.next = None  # reference to next node in DLL
        self.prev = None  # reference to previous node in DLL 
        self.data = item
    
class _DoubleLinkedList:
    """ Implement double linked list"""

    def __init__(self):
        self.head = None
        self.length = 0

    # Add a node at the front 
    def push(self, item):
        new_node = _Node(item)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        self.length += 1

    # Add a node after a given node
    def insertAfter(self, prev_data, item):
        prev_node = self.head
        if prev_node is None:
            print('DLL is empty')
            return None
        
        while prev_node is not None:
            if prev_node.data == prev_data:
                break
            else:
                prev_node = prev_node.next
        

        if prev_node is None:
            print("{} doesn't not exist in DLL".format(prev_data))
            return
        new_node = _Node(item)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

        self.length += 1
       
    def __str__(self):
        tmp = self.head

        if tmp is None:
            print("Double LL is empty")
            return
        
        while tmp is not None:
            print("{} ".format(tmp.data), end=" ")
            tmp = tmp.next
        print()

    # Add a node at the end
    def append(self, item):
        new_node = _Node(item)
        tmp = self.head

        if tmp is None:
            self.head = new_node
            self.head.prev = None
            self.head.next =None
        else:

            while tmp.next is not None:
                tmp = tmp.next
            
            tmp.next = new_node
            new_node.prev = tmp
            new_node.next = None
        self.length += 1


if __name__ == "__main__":
    my_DLL  = _DoubleLinkedList()
    my_DLL.push(1)
    my_DLL.push(2)
    my_DLL.push(3)

    my_DLL.insertAfter(3, 10)
    my_DLL.append(100)
    my_DLL.push(-19)
    my_DLL.append(123)
    my_DLL.__str__()
    print('Length of DLL is {}'.format(my_DLL.length))
