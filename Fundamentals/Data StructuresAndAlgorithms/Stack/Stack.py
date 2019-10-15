class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)    #O(1)
        # self.items.insert(0, item)   #O(n)
    
    def pop(self):
        return self.items.pop() #O(1)

    def peek(self):
        return self.items[len(self.items) - 1] #O(1)
    
    def size(self):
        return len(self.items)

# s1 = Stack()
# print('Size of stack: ', s1.size())
# s1.push(1)
# s1.push(2)
# s1.push(3)

# print('Top of stack: ', s1.peek())
# # s1.pop()
# print("Stack is empty ? ", s1.isEmpty())
# print('Size of stack: ', s1.size())