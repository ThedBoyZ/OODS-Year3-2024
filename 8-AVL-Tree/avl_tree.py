class TreeNode(object): 
    def __init__(self, val): 
        self.data = val 
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self, node = None):
        return -1 if node == None else node.height

    def balanceValue(self):      
        return self.getHeight(self.left) - self.getHeight(self.right)

    def __str__(self):
        return str(self.data)
  
class AVL_Tree(object): 
    def __init__(self, root = None):
        self.root: TreeNode = None if root is None else root

    def insert(self, root, data):
        data = int(data)
        self.root = AVL_Tree._insert(root, data)
        return self.root

    def _insert(root, data):
        if not root:
            return TreeNode(data)
        if data < root.data:
            root.left = AVL_Tree._insert(root.left, data)
        else:
            root.right = AVL_Tree._insert(root.right, data)
        root.setHeight()
        balance = root.balanceValue()
        if balance == -2:
            print("Left Left Rotation")
            if root.right.balanceValue() == 1:
                root.right = AVL_Tree.rotateLeftChild(root.right)
            root = AVL_Tree.rotateRightChild(root)
        elif balance == 2:
            print("Right Right Rotation")
            if root.left.balanceValue() == -1:
                root.left = AVL_Tree.rotateRightChild(root.left)
            root = AVL_Tree.rotateLeftChild(root)
        return root

    def rotateLeftChild(node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.setHeight()
        new_root.setHeight()
        return new_root

    def rotateRightChild(node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.setHeight()
        new_root.setHeight()
        return new_root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")