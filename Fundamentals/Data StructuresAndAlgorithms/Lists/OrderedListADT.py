from moduleNode import Node

class orderedList:

    def __init__(self):
        self.head = None

    def size(self):
        tmp = self.head
        count = 0

        while tmp != None:
            count += 1
            tmp = tmp.next
        return count
    
    def isEmpty(self):
        return self.head == None

    def _search(self, item): #private
        ind = -1
        tmp = self.head

        while tmp != None and tmp.data <= item:
            ind += 1
            if tmp.data == item:
                break
        return ind

    def add(self, item):
        new_node = Node(item)
        previous_node = None
        current_node = self.head

        #Case 2: between of list
        while current_node != None:
            if item < current_node.data:
                previous_node.next = new_node
                new_node.next = current_node
                return
            previous_node = current_node
            current_node = current_node.next
        #Case 1: in front of list
        if previous_node == None:
            new_node.setNext(self.head)
            self.head = new_node
            return 
        #Case 3: item is added at the last of list
        # Now, current_node = None, previous_node != None

        previous_node.next = new_node
        new_node.next = None

    def __str__(self):
        tmp = self.head
        while tmp != None:
            print(tmp.getData(), end=" ")
            tmp = tmp.next
        print()


ordered_list = orderedList()
ordered_list.add(1)
ordered_list.add(3)
ordered_list.add(8)
ordered_list.add(2)
ordered_list.__str__()


