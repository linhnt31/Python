class BinaryTree:
    def __init__(self, data):
        self.key = data
        self.leftchild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            # tmp.leftchild = self.leftchild
            self.leftchild = tmp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            # tmp.rightChild = self.rightChild
            self.rightChild = tmp
        
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftchild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key


if __name__ == "__main__":

    """
            a
           /  \
          b    c
    """ 
    # root = BinaryTree('a')
    # print('Root: ', root.getRootVal())
    
    # root.insertLeft('b')
    # print('Left children: ', root.getLeftChild().getRootVal())

    # root.insertRight('c')
    # print('Right children: ', root.getRightChild().getRootVal())

    # root.getRightChild().setRootVal('Tree')
    # print('After changed right children: ', root.getRightChild().getRootVal())

    """ 
                a
               /  \
              b     c
                \  /  \
                d  e   f
    """

    root = BinaryTree('a')
    root.insertLeft('b')
    root.insertRight('c')
    root.getLeftChild().insertRight('d')
    root.getRightChild().insertLeft('e')
    root.getRightChild().insertRight('f')

    #Left
    print('Root: ', root.getRootVal())
    print('Left children lv1: ', root.getLeftChild().getRootVal())
    print('Right children on the left root lv2: ', root.getLeftChild().getRightChild().getRootVal())
    print('---------------------------------------------------')

    #Right
    print('Right children lv1: ', root.getRightChild().getRootVal())
    print('Left children lv2: ', root.getRightChild().getLeftChild().getRootVal())
    print('Left children lv2: ', root.getRightChild().getRightChild().getRootVal())
