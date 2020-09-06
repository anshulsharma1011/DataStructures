"""
Singly Linked List Implementation

1. Insertion at the END
2. Traverse the list
3. Insert in the BEGINNING
4. Verify if list is sorted
"""


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
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = newNode

    def printList(self):
        currentNode = self.head
        while(currentNode!=None):
            print(currentNode.data,end=" --> ")
            currentNode = currentNode.next
        print("None")

    def insert_beg(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


def sortLinkedList(node):
    return((node is None) or (node.next is None) or ((node.data <= node.next.data) and sortLinkedList(node.next)))

if __name__ == '__main__':
    linked = LinkedList()
    linked.insertEnd(1)
    linked.insertEnd(2)
    linked.insertEnd(3)
    linked.insertEnd(4)
    linked.printList()

    print(sortLinkedList(linked.head))
