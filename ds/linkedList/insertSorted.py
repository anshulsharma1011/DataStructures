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

    def insertSorted(self,data):
        new = Node(data)

        if self.head is None or self.head.data >= data:
            new.next = self.head
            self.head = new

        else:
            begg = self.head
            while begg.next is not None and begg.next.data < data:
                begg = begg.next

            new.next = begg.next
            begg.next = new

if __name__ == '__main__':
    link = LinkedList()
    link.insertSorted(10)
    link.insertSorted(9)
    link.insertSorted(8)
    link.insertSorted(7)
    link.insertSorted(6)
    link.printList()