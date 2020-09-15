"""
1. Insertion in BST.
2. Inorder Traversal
"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNode(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insertNodeInBST(data, self.root)

    def insertNodeInBST(self, data, parent):
        if data < parent.data:
            if parent.left:
                self.insertNodeInBST(data, parent.left)
            else:
                parent.left = Node(data, parent)
        elif data > parent.data:
            if parent.right:
                self.insertNodeInBST(data, parent.right)
            else:
                parent.right = Node(data, parent)

    def traverse(self):
        root = self.root
        if root is not None:
            self.traverse_in_order(root)

    def traverse_in_order(self, root):
        if root.left:
            self.traverse_in_order(root.left)

        print("%s" % root.data)

        if root.right:
            self.traverse_in_order(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insertNode(10)
    bst.insertNode(9)
    bst.insertNode(8)
    bst.insertNode(7)
    bst.insertNode(6)
    bst.insertNode(5)
    bst.insertNode(4)
    bst.insertNode(3)
    bst.traverse()
