""" 
- Create an implementation of a queue that would have an average performance of O(1) for enqueue and dequeue operations.
"""

class Node:
    
    def __init__(self, item):
        self.next = None
        self.data = item

class Queue:
    """ Implement Queue by linked list """

    #Time complexity for enqueue() and dequeue() is O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Time complexity: O(1)
    def enqueue(self, item):
        new_node = Node(item)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = self.head
        self.length += 1

    #Time complexity: O(1)
    def dequeue(self):
        pass
        
    def size(self):
        return self.length

    def __str__(self):
        tmp = self.head

        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)

    my_queue.__str__()
    print("Size of Queue is {}".format(my_queue.size()))