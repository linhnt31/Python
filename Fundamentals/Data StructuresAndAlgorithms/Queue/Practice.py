class implementQueue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item) #O(n)
    
    def dequeue(self):
        return self.items.pop() #O(1)
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


#Exercise : potato

def potato(peopleList, step):
    simqueue = implementQueue()
    for people in peopleList:
        simqueue.enqueue(people)
    
    while simqueue.size() > 1:
        for _ in range(0, step):
            simqueue.enqueue(simqueue.dequeue())
        
        simqueue.dequeue()
    return simqueue.dequeue()

if __name__ == "__main__":
    peopleList = ['a', 'b', 'c', 'd']
    step = 6
    print(potato(peopleList, step))