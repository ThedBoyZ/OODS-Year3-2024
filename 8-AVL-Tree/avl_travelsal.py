class AVLNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.height = self.setHeight()
    
    def __str__(self):
        return str(self.data)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self, node = None):
        return -1 if node == None else node.height
    
    def balanceValue(self):      
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVLTree:
    def __init__(self, root = None):
        self.root: AVLNode = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, int(data))

    def _add(root, data):
        if not root:
            return AVLNode(data)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root.setHeight()
        balance = root.balanceValue()
        if balance == -2:
            if root.right.balanceValue() == 1:
                root.right = AVLTree.rotateLeftChild(root.right)
            root = AVLTree.rotateRightChild(root)
        elif balance == 2:
            if root.left.balanceValue() == -1:
                root.left = AVLTree.rotateRightChild(root.left)
            root = AVLTree.rotateLeftChild(root)
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

    def postOrder(self):
        print("AVLTree post-order : ", end="")
        self._postOrder(self.root)
        print()

    def _postOrder(self, node):
        if node is None:
            return
        if node.left:
            self._postOrder(node.left)
        if node.right:
            self._postOrder(node.right)
        print(node.data, end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node, level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()