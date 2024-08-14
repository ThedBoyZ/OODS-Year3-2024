class Queue():
    def __init__(self, items=None, max=None, ) -> None:
        if items is None:
            self.items = []
        else:
            self.items = items
        
        self.max = max
    
    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def isEmpty(self):
        return len(self) == 0

    def isFull(self):
        if self.max is not None:
            return len(self) == self.max
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def enQueue(self, x):
        if not self.isFull():
            self.items.append(x)

class Canteen(Queue):
    def __init__(self, id:list, queue:list):
        super().__init__()
        self.id = id
        self.queue = queue
    
    def checkIndex(self, x):
        if self.isEmpty():
            return 0
        idx = 0
        c = 0
        for index, e in enumerate(self):
            if e[0] == x[0]:
                if index > idx:
                    idx = index
                c += 1
        if idx == 0 and c == 0:
            return len(self)
        return idx + 1

    def check(self, x):     
        if self.isEmpty():
            self.enQueue(x)
        else:
            idx = self.checkIndex(x)
            self.items.insert(idx, x)
                
            
    def solve(self):
        for index, q in enumerate(self.queue):
            if len(q) > 1:
                q = q.split()
                self.check(q[1])
            else:
                if self.isEmpty():
                    print('Empty')
                else:
                    print(self.deQueue())
        


inp = input('Enter Input : ').split('/')

employee = inp[0].split(',')
queue = inp[1].split(',')
canteen = Canteen(employee, queue)
canteen.solve()