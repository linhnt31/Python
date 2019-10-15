"""
Implement a queue using linked lists.
"""

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class Queue: #FIFO
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def enqueue(self, item): #O(1)
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def dequeue(self): #O(n)
        if self.head is None:
            print("Queue is empty !!! Cant dequeue")
            return None
        
        current_node = self.head
        previous_node = None

        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next

        self.length -= 1
        previous_node.next = None
        return current_node.data

    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        tmp = self.head

        while tmp != None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    #Obj of class Queue
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)

    my_queue.__str__()

    print('Before dequeuing element: {} items'.format(my_queue.size()))
    last_item = my_queue.dequeue()
    print('last element is {}'.format(last_item))
    print('After dequeuing element: {} items'.format(my_queue.size()))

    my_queue.__str__()