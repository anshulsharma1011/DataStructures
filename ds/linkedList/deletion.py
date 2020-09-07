"""
1. Delete Node with given Data
2. POP operation
3. Delete Complete List
4. Delete every N nodes in a linked list after skipping M nodes
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.point = 0

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" --> ")
            currentNode = currentNode.next
        print("None")

    def insert_beg(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        actualNode = self.head

        if self.head is None:
            self.head = newNode
        else:
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = newNode

    def deleteNode(self,param):
        if self.head is None:
            return
        actualNode = self.head
        if actualNode.data == param:
            self.head = actualNode.next
        else:
            while actualNode.next is not None and actualNode.next.data != param:
                actualNode = actualNode.next
            if actualNode.next is None:
                return
            actualNode.next = actualNode.next.next
        actualNode = None

    def deleteNode2(self,param):
        if self.head is None:
            return
        actualNode = self.head
        previousNode = None

        while actualNode is not None and actualNode.data != param:
            previousNode = actualNode
            actualNode = actualNode.next

        if actualNode is None:
            return

        if previousNode is None:
            self.head = actualNode.next

        else:
            previousNode.next = actualNode.next
        actualNode = None

    def popData(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        return temp.data


def deleteAll(linkedList):
    headPointer = linkedList.head

    while headPointer is not None:
        linkedList.deleteNode(headPointer.data)
        headPointer = headPointer.next

def deleteMNNodes(head, m, n):
    # base case
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr:
        # skip m nodes
        for i in range(1, m + 1):
            prev = curr
            curr = curr.next

        # delete next n nodes
        for i in range(1, n + 1):
            if curr:
                curr = curr.next
                
        # link remaining nodes with last node
        prev.next = curr
        # recur for remaining nodes
        # deleteNodes(curr, m, n)
    return head

if __name__ == '__main__':
    link = LinkedList()
    link.insertEnd(53)
    link.insertEnd(53)
    link.insertEnd(49)
    link.insertEnd(49)
    link.insertEnd(35)
    link.insertEnd(28)
    link.printList()
    link.deleteNode(8)
    link.removeAllDuplicates(link.head)
    link.printList()
