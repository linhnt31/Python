class Stack:
    '''implemeting class Stack by my hands '''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) <= 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def __str__(self):
        while len(self.items) > 0:
            print('| {} |'.format(self.items.pop()))
            print('------')
        print()