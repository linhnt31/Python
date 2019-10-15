class _Queue:
    """ Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list."""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item) #O(1)
    
    def dequeue(self):
        try:
          return self.items.pop(0)
        except IndexError as e:
            print(e)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def __str__(self):
        print(str(self.items))
#Ooj

my_queue = _Queue()
my_queue.dequeue()

# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(4)

# print(my_queue.dequeue())
my_queue.__str__()