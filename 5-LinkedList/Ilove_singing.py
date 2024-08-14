class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def appendHead(self, value):
        node = Node(value, self.head)
        self.head = node

    def appendLast(self, value):
        if self.head is None:
            self.appendHead(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def removeLast(self):
        if self.head is None:
            return "Error!!!"
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def rename(self, newName):
        if self.head is None:
            return "Error!!!"
        current = self.head
        while current.next:
            current = current.next
        current.value = newName

    def printList(self):
        if self.head is None:
            print("Linklist is empty!")
            return
        current = self.head
        while current is not None:
            print(current.value, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()

    def printListWithNoDuplicate(self):
        if self.head is None:
            print("Linklist is empty!")
            return
        seen = set()
        current = self.head
        first = True 
        while current:
            if current.value not in seen:
                seen.add(current.value)
                if not first:
                    print(" -> ", end="")
                print(current.value, end="")
                first = False
            current = current.next
        print()

def convertToLinkList(ls):
    ll = LinkList()
    for item in ls:
        ll.appendLast(item)
    return ll

print("*** My Favourite Keynote ***")
inputl = input("Enter Input / List of operation : ").split('/')
listSong = [ele for ele in inputl[0].strip().split(' ')]
operations = [ele for ele in inputl[1].strip().split(", ")]
myLinkList = convertToLinkList(listSong)
myLinkList.printList()

error_flag = False
for operation in operations:
    if operation.startswith("A "):
        note = operation.split(" ")[1]
        myLinkList.appendLast(note)
    elif operation.startswith("D"):
        result = myLinkList.removeLast()
        if result == "Error!!!":
            print(result)
            error_flag = True
    elif operation.startswith("R "):
        new_name = operation.split(" ")[1]
        result = myLinkList.rename(new_name)
        if result == "Error!!!":
            print(result)

if not error_flag:
    myLinkList.printList()
else:
    print("Linklist is empty!")

myLinkList.printListWithNoDuplicate()
