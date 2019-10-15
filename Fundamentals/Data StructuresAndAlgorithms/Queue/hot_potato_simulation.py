from pythonds.basic.queue import Queue

def hotPotato(nameList, num):
    sim_queue = Queue()
    for name in nameList:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()
    return sim_queue.dequeue()

if __name__ == "__main__":
    nameList = ["Bill","David","Susan","Jane","Kent","Brad"]
    num = 2
    print(hotPotato(nameList, num))