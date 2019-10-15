class binaryTree:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insertLeft(self, newNode):
        tmp = binaryTree(newNode)
        if self.left_child == None:
            self.left_child = tmp
        else:
            
    
    def insertRight(self, newNode):
        pass
    
    def getLeftChild(self):
        pass

    def getRightChild(self):
        pass

    def getRootVal(self):
        pass
    

if __name__ == "__main__":
    pass