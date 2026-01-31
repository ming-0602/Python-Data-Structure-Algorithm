class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():

    def __init__(self):
        self.root = None


    def insert(self, value):
        self.root = self.insertrec(self.root, value)

    def insertrec(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insertrec(root.left, value)
        else:
            root.right = self.insertrec(root.right, value)
        return root

    def printorder(self):
        self.printorderrec(self.root)
        print()

    def printorderrec(self, root):
        if root is not None:
            print(f'{root.value}', end=' ')
            self.printorderrec(root.left)
            self.printorderrec(root.right)

    def printinorder(self):
        self.printinorderrec(self.root)
        print()

    def printinorderrec(self, root):
        if root is not None:
            self.printinorderrec(root.left)
            print(f'{root.value}', end=' ')
            self.printinorderrec(root.right)




tree = BinaryTree()
tree.insert(8)
tree.insert(7)
tree.insert(12)
tree.insert(15)
tree.insert(2)
tree.insert(5)

tree.printorder()
tree.printinorder()