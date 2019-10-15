""" 
 Implement a deque using linked lists.
"""


class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class _Deque:
    """ Implement a deque using linked lists. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addFront(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head
        self.length += 1
    
    def addRear(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.length += 1

    def removeFront(self):
        if self.head is None:
            print('Deque is empty')
            return None
        
        #release memory for first Node
        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1

    def removeRear(self):
        pre_node = self.head

        if self.isEmpty(): 
            print('Deque is empty')
            return None
        
        if self.head.next is None: # length of deque is 1
            self.tail = self.head = None
            self.length -= 1
            return None

        while pre_node.next.next is not None:
            pre_node = pre_node.next

        self.tail = pre_node
        self.tail.next = None
        self.length -= 1
    
    def size(self):
        return self.length

    def isEmpty(self):
        return  self.head == None

    def __str__(self):
        tmp = self.head
        if tmp is None:
            print('Deque is empty')
            return None

        while tmp is not None:
            print("{} ".format(tmp.data),end=" ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    my_deque = _Deque()
    # my_deque.addFront(1)
    # my_deque.addFront(2)

    # my_deque.removeFront()

    # my_deque.addRear(1)
    # my_deque.addFront(2)
    # my_deque.addFront(3)
    # my_deque.addRear(5)

    # my_deque.removeRear()

    #all test case
    # my_deque.addFront(1)
    # my_deque.addRear(2)
    # my_deque.addFront(3)
    # my_deque.addRear(4)

    my_deque.removeRear()
    my_deque.addFront(6)
    my_deque.addRear(10)

    my_deque.removeFront()

    my_deque.__str__()
    print('Length of deque is {}'.format(my_deque.length))