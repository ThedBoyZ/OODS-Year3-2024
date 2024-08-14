class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)
           
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return str(len(self.items))

    #def returnStack(self):  
        #return self.items

def postFixeval(st):

    s = Stack()
    for i in st:
        if i == '+':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) + float(obj1)
            s.push(obj)
        elif i == '-':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) - float(obj1)
            s.push(obj)
        elif i == '*':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) * float(obj1)
            s.push(obj)
        elif i == '/':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) / float(obj1)
            s.push(obj)
        else:
            s.push(i)
        #print(s.returnStack())
    return s.pop()

            
print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))