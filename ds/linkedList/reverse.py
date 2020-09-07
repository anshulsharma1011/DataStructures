"""
1. Reverse LL (Iterative)
2. Reverse LL (Recursive)
3. Reverse every group of k nodes
"""

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data,end=" --> ")
        ptr = ptr.next
    print("None")


def reverseIterate(s):
    p = q = None
    while s:
        p = q
        q = s
        s = s.next
        q.next = p
    s = q
    return s


def reverseRecursive(head,headRef=None):
    if head is None:
        return None

    first = head
    rest = head.next

    if rest is None:
        return first

    headRef = reverseRecursive(rest,headRef)
    rest.next = first
    first.next = None

    return headRef


def reverseGroup(head,k):
    if head is None:
        return None

    current = head
    prev = None
    count = 0
    while current and count < k:
        count += 1
        next = current.next
        current.next = prev
        prev = current
        current = next

    head.next = reverseGroup(current,k)
    return prev

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
                next = curr.next
                curr = next
        # link remaining nodes with last node
        prev.next = curr
        # recur for remaining nodes
        # deleteNodes(curr, m, n)
    return head

if __name__ == '__main__':
    linkData = [1,2,3,4,5,6,7,8,9,10]
    head = None
    for i in reversed(linkData):
        head = Node(i,head)

    printList(head)
    print("---->")
    printList(deleteMNNodes(head,2,2))
