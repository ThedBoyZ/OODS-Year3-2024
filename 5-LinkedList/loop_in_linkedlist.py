class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.dummy = self.Node(None, None)
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty'
        s = ''
        p = self.dummy.next
        while p != None:
            s += str(p.data) + '->'
            p = p.next
        return s[:-2]

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.dummy.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.dummy
        for j in range(-1, i):
            p = p.next
            if p.next == None:
                break
        return p

    def append(self, data):
        return self.insertAfter(len(self), data)

    def insertAfter(self, i, data):
        p = self.nodeAt(i-1)
        p.next = self.Node(data, p.next)
        self.size += 1

    def deleteAfter(self, i):
        if self.size > 0:
            p = self.nodeAt(i)
            p.next = p.next.next
            self.size -= 1

    def delete(self, i):  
        self.deleteAfter(i-1)

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)
ll=LinkedList()
countl=0
inp=input('Enter input : ').split(',')
for i in inp:
    if(i[0]=='A'):
        ll.append(int(i[1:]))
        print(ll.__str__())
    elif(i[0]=='S'):
        i=i.split(':')
        if(ll.isEmpty()):
            print('Error! {list is empty}')
        elif(int(i[0][2:])>ll.size-1 ):
            print('Error! {index not in length}: '+i[0][2:])
        elif(int(i[1])>ll.size-1):
            ll.append(int(i[1]))
            print('index not in length, append : '+i[1])
        elif(int(i[0][2:])<=ll.size-1 and int(i[0][2:])>=int(i[1])):
            n1 = ll.nodeAt(int(i[0][2:]))
            n2 = ll.nodeAt(int(i[1]))
            n1.next = n2
            print('Set node.next complete!, index:value = '+(i[0][2:]) + ':'+str(n1.data) +' -> '+i[1] + ':'+ str(n2.data))
            countl+=1
        elif(int(i[1])<=ll.size-1 and int(i[0][2:])<int(i[1])):
            n1 = ll.nodeAt(int(i[0][2:]))
            n2 = ll.nodeAt(int(i[1]))
            n1.next = n2
            print('Set node.next complete!, index:value = '+(i[0][2:]) + ':'+str(n1.data) +' -> '+i[1] + ':'+ str(n2.data))
if(countl==0 and ll.isEmpty()==0):
    print('No Loop')
    print(ll.__str__())
elif(countl>0):
    print('Found Loop')
if(ll.isEmpty()):
    print('No Loop')
    print('Empty')