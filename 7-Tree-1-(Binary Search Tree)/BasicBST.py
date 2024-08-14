class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
            
    def insert_recursive(self, node, value):
        if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self.insert_recursive(node.left, value)       
        elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self.insert_recursive(node.right, value)       
                    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    # def search(self, value):
    #     return self.search_recursive(self.root, value)

    # def search_recursive(self, node, value):
    #     if node is None or node.value == value:
    #         return node
    #     if value < node.value:
    #         self.search_recursive(node.left, value)
    #     else:
    #         self.search_recursive(node.right, value)            

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)