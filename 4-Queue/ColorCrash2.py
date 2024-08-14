class Queue:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)
    
    def isEmpty(self):
        return len(self.store) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.store[0]
        return
    
    def enqueue(self,element):
        self.store.append(element)
    
    def dequeue(self,i):
        if not self.isEmpty() and len(self.store) > i:
            return self.store.pop(i)
        return
    
    def adjust_original(self,ele:list):
        adjust = []
        fail = 0
        for i in range(1,len(self.store)-1):
            if self.store[i-1] == self.store[i] == self.store[i+1] : 
                adjust.append(i+1)   
        while len(adjust) > 0 and len(ele) > 0 :
            if ele[0] == self.store[adjust[0]-1]:
                fail += 1
            self.store.insert(adjust.pop(0),ele.pop(0))
            for i in range(len(adjust)):
                adjust[i] += 1
        self.store.reverse()
        return fail

    def crush2(self):
        run = True
        number = 0
        while run :
            run = False
            for i in range(1,len(self.store)-1):
                if self.store[i-1] == self.store[i] == self.store[i+1] :
                    for j in range(3):
                        self.dequeue(i-1)
                    number += 1
                    run = True
                    break
        self.store.reverse()
        return number,self.store
    
    def crush(self):
        run = True
        res = []
        delete = []
        last= [-1,-1,-1]
        number = 0
        while run :
            run = False
            for i in range(1,len(self.store)-1):
                if self.store[i-1] == self.store[i] == self.store[i+1] and (i-1 not in last) and (i not in last) and (i+1 not in last) :
                    delete.append(i-1)
                    run = True
                    last = [i-1,i,i+1]
                    number += 1
            delete.reverse()
            for i in delete :
                res.append(self.store[i])
                for j in range(3):
                    self.dequeue(i)
            delete = []     
        return res,number
    
class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.isEmpty():
      return self.items.pop()
    return None

  def peek(self):
    if not self.isEmpty():
      return self.items[-1]
    return None

  def size(self):
    return len(self.items)

def PrintArr(ls:list,mode):
    stg = ""
    if mode :
        for i in range(len(ls)-1,-1,-1):
            stg += ls[i]
    else :
        for i in range(len(ls)):
            stg += ls[i]
    print(stg)

def main():
    real,mirror  = input('Enter Input (Normal, Mirror) : ').split()
    ls_real = list(real)
    ls_mirror = list(mirror)
    Q1 = Queue()
    Q1.store = ls_mirror
    Q2 = Queue()
    Q2.store = ls_real
    items = Q1.crush()
    fail = Q2.adjust_original(items[0])
    number_normal,out_normal = Q2.crush2()
    out_mirror = Q1.store
    print("NORMAL :")
    print(len(out_normal))
    if len(out_normal) :
        PrintArr(out_normal,1)
    else :
        print("Empty")
    print(f"{number_normal-fail} Explosive(s) ! ! ! (NORMAL)")
    if fail :
        print(f"Failed Interrupted {fail} Bomb(s)")
    print("------------MIRROR------------")
    print(': RORRIM')
    print(len(out_mirror))
    if len(out_mirror) :
        PrintArr(out_mirror,0)
    else :
        print("ytpmE")
    print(f"(RORRIM) ! ! ! (s)evisolpxE {items[1]}")

if __name__ == "__main__":
    main()