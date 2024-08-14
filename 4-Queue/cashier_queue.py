class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

people, t = input("Enter people and time : ").split()
count = 1
m = Queue()
c1 = Queue()
t1 = 1
c2 = Queue()
t2 = 1

for i in people:
    m.enQueue(i)

while count <= int(t):
    if not c1.isEmpty():
        if t1 == 3:
            c1.deQueue()
            t1 = 1
        else:
            t1 += 1

    if not c2.isEmpty():
        if t2 == 2:
            c2.deQueue()
            t2 = 1
        else:
            t2 += 1
    if c1.size() < 5:
       
        if not m.isEmpty():
            c1.enQueue(m.deQueue())
        else:
            pass
    elif c2.size() < 5:      
        if not m.isEmpty():
            c2.enQueue(m.deQueue())
        else:
            pass
    print(count, m.items, c1.items, c2.items)
    count += 1