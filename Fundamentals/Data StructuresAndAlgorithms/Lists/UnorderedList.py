from moduleNode import Node
import pdb


class unorderedList:
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        tmp = self.head
        size_ = 0
        while tmp != None:
            size_ += 1
            tmp = tmp.next

        return size_

    def search(self, item):
        tmp = self.head

        found = False
        while tmp != None and not found:
            if tmp.getData() == item:
                found = True
            tmp = tmp.getNext()
        
        return found


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        elif not current == None:
            previous.setNext(current.getNext())

    #O(n)   
    def append(self, item):
        tmp = self.head
        newNode = Node(item)

        while tmp.next != None:
            tmp = tmp.next
        tmp.next = newNode
        newNode.next = None

    def pop(self):
        #list is empty
        if self.head == None:
            return -1
        if self.head.next == None:
            return self.head.data
        pre_node = None
        current_node = self.head

        while current_node.next != None:
            pre_node = current_node
            current_node = current_node.next
        
        tmp = current_node.data
        pre_node.next = None
        return tmp

    def index(self, item):
        ind = -1
        tmp = self.head

        while tmp != None:
            ind += 1
            if tmp.data == item:
                return ind
            tmp = tmp.next
        return -1

    #O(1) time
    def insert(self, item, position):
        new_node = Node(item)
        len_ = self.size()
        previous_node = None
        current_node = self.head

        if position < 0 or position >= len_:
            print('OutOfIndex: position not found')
            return 
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        for _ in range(position):
            previous_node = current_node
            current_node = current_node.next
        
        previous_node.next = new_node
        new_node.next = current_node

    def __str__(self):
        tmp = self.head
        while tmp != None:
            print(tmp.getData(), end=" ")
            tmp = tmp.next
        print()


my_list = unorderedList()
my_list.add(1)
my_list.add(10)
my_list.add(6)
my_list.add(8)

# my_list.remove(1)
# my_list.__str__()
# print(my_list.size())
# print(my_list.search(8))
# my_list.append(100)
# my_list.__str__()

# print('element is popped: {}'.format(my_list.pop()))
# my_list.__str__()

# print('index of {} is {}'.format(78,  my_list.index(8)))

my_list.__str__()
print('Size of list is {}'.format(my_list.size()))
my_list.insert(100, 3)
my_list.__str__()

# my_list.insert(123, 4)
# my_list.__str__()