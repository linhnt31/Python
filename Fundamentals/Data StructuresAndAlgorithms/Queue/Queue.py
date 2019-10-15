class Queue:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item) #O(n)
    
    def dequeue(self):
        return self.items.pop() # O(1)
    
    def size(self):
        return len(self.items)

    
#Object
# q = Queue()

# print(q.isEmpty())
# q.enqueue(1)
# q.enqueue(2)
# q.dequeue()
# print(q.size())