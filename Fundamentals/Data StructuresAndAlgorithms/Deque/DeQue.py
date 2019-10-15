class Deque:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.append(item) #O(1)

    def addRear(self, item):
        self.items.insert(0, item) #O(n)
    
    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

#Obj

# test_deque = Deque()
# test_deque.addFront(10)
# test_deque.addFront(0)
# test_deque.addFront(1)
# test_deque.addRear(100)

# a = test_deque.removeFront()
# print(a)
# print(test_deque.size(), test_deque.isEmpty())
# print(test_deque)
    
