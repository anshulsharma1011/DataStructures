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


'''
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
'''


def insertNode(data, root):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insertNode(data, root.left)

    else:
        root.right = insertNode(data, root.right)

    return root


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print("%d" % root.data, end=" ")
    inorderTraversal(root.right)


if __name__ == '__main__':
    root = None
    list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for i in list:
        root = insertNode(i, root)

    inorderTraversal(root)
