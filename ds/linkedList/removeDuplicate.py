"""
1. Remove Duplicate Nodes from a sorted linked list

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
        actualNode = self.head
        if not self.head:
            self.head = newNode
        else:
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = newNode

    def printList(self):
        currentNode = self.head
        while(currentNode!=None):
            print(currentNode.data,end=" --> ")
            currentNode = currentNode.next
        print("None")


def removeDuplicates(originalList):
    current = originalList.head
    if current is None:
        return originalList
    while current.next:
        if current.data == current.next.data:
            temp = current.next
            current.next = current.next.next
            temp = None
        else:
            current = current.next
    return originalList


if __name__ == '__main__':
    link = LinkedList()

    link.insertEnd(1)
    link.insertEnd(2)
    link.insertEnd(2)
    link.insertEnd(2)
    link.insertEnd(3)
    link.insertEnd(4)
    link.insertEnd(4)
    link.insertEnd(5)
    link.printList()
    link2 = removeDuplicates(link)
    link2.printList()
