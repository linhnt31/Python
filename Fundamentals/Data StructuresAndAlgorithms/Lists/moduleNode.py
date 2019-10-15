class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

# tmp = Node(20)
# tmp.setData(16)
# print(tmp.getData())