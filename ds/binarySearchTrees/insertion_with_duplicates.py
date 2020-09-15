"""
1. Insertion in BST with duplicate values
2. In-order Traversal
"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.count = 1

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
        else:
            parent.count += 1

    def traverse(self):
        root = self.root
        if root is not None:
            self.traverse_in_order(root)

    def traverse_in_order(self, root):
        if root.left:
            self.traverse_in_order(root.left)

        print("%s (%s)" % (root.data,root.count),end=" ")

        if root.right:
            self.traverse_in_order(root.right)

'''

def insertNode(data, root):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insertNode(data, root.left)

    elif data > root.data:
        root.right = insertNode(data, root.right)

    else:
        root.count += 1

    return root


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print("%d (%d)" % (root.data,root.count), end=" ")
    inorderTraversal(root.right)



if __name__ == '__main__':
    root= None
    list = [12, 10, 20, 9, 11, 10, 12, 12]
    for i in list:
        root = insertNode(i, root)

    inorderTraversal(root)