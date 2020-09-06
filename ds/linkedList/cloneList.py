class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)
        actualNode = self.head

        if self.head==None:
            self.head = newNode
        else:
            while actualNode.next!=None:
                actualNode = actualNode.next
            actualNode.next = newNode

    def printList(self):
        currentNode = self.head
        while(currentNode!=None):
            print(currentNode.data,end=" --> ")
            currentNode = currentNode.next
        print("None")


def duplicateList(original):
    originalHead = original.head

    newList = LinkedList()

    while originalHead is not None:
        newList.insertEnd(originalHead.data)
        originalHead = originalHead.next

    return newList

if __name__ == '__main__':
    link = LinkedList()
    link.insertEnd(4)
    link.insertEnd(5)
    link.insertEnd(6)
    link.insertEnd(7)
    link.insertEnd(8)

    link.printList()

    newLinkedList = duplicateList(link)
    newLinkedList.printList()