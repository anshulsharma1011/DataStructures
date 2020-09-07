"""
1. Intersection of two sorted linked list

"""

class Node:
    def __init__(self, data=None):
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

def printFromHead(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" --> ")
        ptr = ptr.next
    print("None")

def sortedIntersection(linkA,linkB):
    head = tail = None
    a = linkA.head
    b = linkB.head
    while a and b:
        if a.data == b.data:
            if head is None:
                head = Node(a.data)
                tail = head
            else:
                tail.next = Node(a.data)
                tail = tail.next
            a = a.next
            b = b.next

        elif a.data < b.data:
            a = a.next

        else:
            b = b.next
    return head

if __name__ == '__main__':
    link = LinkedList()
    link.insertEnd(1)
    link.insertEnd(4)
    link.insertEnd(7)
    link.insertEnd(10)

    link2 = LinkedList()
    link2.insertEnd(2)
    link2.insertEnd(4)
    link2.insertEnd(6)
    link2.insertEnd(8)
    link2.insertEnd(10)

    link.printList()
    link2.printList()
    print("----->")
    printFromHead(sortedIntersection(link,link2))