"""
Implement a stack using linked lists.
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self):
        if self.head is None:
            print("Queue is empty")
            return None

        current_node = self.head
        self.head = self.head.next

        self.length -= 1
        return current_node.data
        
    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        tmp = self.head

        while tmp != None:
            print("|  {}  |".format(tmp.data))
            print("--------")
            tmp = tmp.next
        print()

#OBJ

my_stack = Stack()

# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(4)

my_stack.pop()

my_stack.__str__()