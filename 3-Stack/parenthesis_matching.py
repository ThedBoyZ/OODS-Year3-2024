class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, items):
        self.items.append(items)
        
    def pop(self):
        items = self.items[-1]
        self.items.remove(items)
        return items
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]
    
s = Stack()
p = ["(","{","["]
q = [")","}","]"]
inp = input("Enter expresion : ")
print(inp, end="")

for items in inp:
    if items in p:
        s.push(items)
    elif items in q:
        if s.size() == 0:
            print(" close paren excess")
            exit()
        elif p.index(s.top()) != q.index(items):
            print(" Unmatch open-close")
            exit()
        else:
            s.pop()
            
if s.size() != 0:
    print(" open paren excess   "+str(s.size())+" : ",end="")
    r = ""
    while not s.isEmpty():
        r += s.top()
        s.pop()
    print(r[::-1])
else:
    print(" MATCH")