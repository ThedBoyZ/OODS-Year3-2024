class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def addHead(self, item):
        node = Node(item)
        if not self.head:
            self.head = self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insert(self, pos, item):
       if pos >= self.size():
           self.append(item)
           return
       elif pos <= -self.size():
           self.addHead(item)
           return
       
       node = Node(item)
       size = -self.size()
       current_node = self.head
       while size != pos:
           current_node = current_node.next
           if current_node == None:
               current_node = self.head
           size += 1
       current_node.prev.next = node
       node.next = current_node
       node.prev = current_node.prev
       current_node.prev = node

    def search(self, item):
        current_node = self.head
        while current_node:
            if current_node.value == item:
                return "Found"
            current_node = current_node.next
        return "Not Found"

    def index(self, item):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == item:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def size(self):
        current_node = self.head
        index = 0
        while current_node:
            index += 1
            current_node = current_node.next
        return index


    def pop(self, pos):
        length = self.size()
        
        if not (-length <= pos < length):
            return "Out of Range"
        
        if pos < 0:
            pos += length
        
        current_node = self.head
        p = 0

        while p != pos:
            p += 1 
            current_node = current_node.next

            if current_node is None:
                current_node = self.head
        
        if current_node == self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            current_node.next = None
            return "Success"
        
        if current_node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            current_node.prev = None
            return "Success"
        
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return "Success"
    
L = DoublyLinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())