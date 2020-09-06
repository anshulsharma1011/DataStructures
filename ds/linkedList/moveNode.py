"""
1. Move front node of the given list to the front of the another list
2. Move even nodes to the end of the list in reverse order
3. Construct a linked list by merging alternate nodes of two given lists
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        currentNode = self.head
        while(currentNode!=None):
            print(currentNode.data,end=" --> ")
            currentNode = currentNode.next
        print("None")

    def insertEnd(self, data):
        newNode = Node(data)
        actualNode = self.head

        if self.head==None:
            self.head = newNode
        else:
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = newNode

    def insertBeg(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def deleteFromBeg(self):
        if not self.head:
            return None
        self.head = self.head.next


def moveFrontNode(list1,list2):
    if not list2.head:
        return
    list1.insertBeg(list2.head.data)
    list2.deleteFromBeg()


def moveEvenNodes(originalList):
    current = originalList.head

    if not current:
        return

    odd = current
    even = prev = None

    while odd and odd.next:
        if odd.next:
            newNode = odd.next
            odd.next = odd.next.next
            newNode.next = even
            even = newNode

        prev = odd
        odd = odd.next

    if odd:
        odd.next = even
    else:
        prev.next = even


def mergeAlternate(list1,list2):
    newList = LinkedList()
    head1 = list1.head
    head2 = list2.head

    if not head1:
        return
    if not head2:
        return

    while True:
        if head1:
            newList.insertEnd(head1.data)
            head1 = head1.next
        if head2:
            newList.insertEnd(head2.data)
            head2 = head2.next
        if head1 is None and head2 is None:
            break

    newList.printList()

def insertNode(source,data):
    newNode = Node(data)
    if source is not None:
        source.next = newNode
        return source.next
    return newNode

def mergeAlternate2(link1,link2):
    dummy = Node()
    tail = dummy

    while True:
        if a is None:
            tail.next = b
            break
        elif b is None:
            tail.next = a
            break
        else:
            tail.next = a
            tail = a
            a = a.next

            tail.next = b
            tail = b
            b = b.next
    return dummy.next

if __name__ == '__main__':
    linked = LinkedList()
    linked.insertEnd(1)
    linked.insertEnd(3)
    linked.insertEnd(5)
    linked.insertEnd(7)
    linked.insertEnd(9)
    linked.insertEnd(11)
    linked.printList()

    linked2 = LinkedList()
    linked2.insertEnd(2)
    linked2.insertEnd(4)
    linked2.insertEnd(6)
    linked2.insertEnd(8)
    linked2.insertEnd(10)
    linked2.printList()
    print("------------")

    mergeAlternate2(linked,linked2)