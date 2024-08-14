class Queue:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)
    
    def isEmpty(self):
        return len(self.store) == 0
    
    def enqueue(self,element):
        self.store.append(element)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.store.pop(0)
        return
if __name__ == "__main__":
    inps = [e for e in input("Enter Input : ").split('/')]
    shelf = [int(e) for e in inps[0].split(" ")]
    Q1 = Queue()
    
    for ele in shelf :
        Q1.enqueue(ele)
    command = inps[1].split(',')
    
    while len(command):
        each = command.pop(0)
        if each == 'D':
            Q1.dequeue()
        else :
            value = int(each.split(' ')[1])
            Q1.enqueue(value)
    flag = False
    for i in Q1.store:
        if Q1.store.count(i) > 1 :
            print("Duplicate")
            flag = True
            break
    if not flag :
        print('NO Duplicate')