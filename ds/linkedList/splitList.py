"""
1. Split list into first and last halves
2. Split in alternates
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def printList(self):
        currentNode = self.head
        while(currentNode!=None):
            print(currentNode.data,end=" --> ")
            currentNode = currentNode.next
        print("None")

def getMidElement(linkedList):
    p = q = linkedList.head
    while q is not None and q.next is not None and q.next.next is not None:
        p = p.next
        q = q.next.next
    return p

def getHalfList(type,midNode,link):
    if type == 'start':
        currentNode = link.head
        while currentNode != midNode.next:
            print(currentNode.data, end=" --> ")
            currentNode = currentNode.next
        print("None")
    else:
        currentNode = midNode.next
        while currentNode is not None:
            print(currentNode.data, end=" --> ")
            currentNode = currentNode.next
        print("None")

def splitAlternate(originalList):
    listA = LinkedList()
    listB = LinkedList()
    if not originalList.head:
        return

    current = originalList.head
    while current:
        listA.insertEnd(current.data)
        current = current.next
        if current:
            listB.insertEnd(current.data)
            current = current.next00

    listA.printList()
    listB.printList()

if __name__ == '__main__':
    link = LinkedList()
    link.insertEnd(1)
    link.insertEnd(2)
    link.insertEnd(3)
    link.insertEnd(4)
    link.insertEnd(5)
    link.insertEnd(6)
    link.insertEnd(7)
    link.printList()
    splitAlternate(link)
