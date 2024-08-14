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
            
    def printSorted(self, number_compare):
        sorted_value = self.in_order_traversal(self.root, number_compare)
        result = ' '.join(map(str,sorted_value))
        if len(sorted_value) == 0:
            print(f"Below {number_compare} : Not have")
        else:
            print(f"Below {number_compare} : {result}")            
        
    def in_order_traversal(self, node, number_compare):
        values = []
        if node is not None:
            values.extend(self.in_order_traversal(node.left, number_compare))
            if node.value < number_compare:
                values.append(node.value)
            values.extend(self.in_order_traversal(node.right , number_compare))
        return values       
    

            

T = BST()
str_tree = input('Enter Input : ')
number_compare = str_tree.split('|')
inp = [int(i) for i in number_compare[0].split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)    
print("--------------------------------------------------")
T.printSorted(int(number_compare[1]))