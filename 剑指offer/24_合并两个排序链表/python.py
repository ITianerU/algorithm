"""

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1, pHead2):
    while pHead2:
        newNode = ListNode(pHead2.val)
        pHead1 = hb(pHead1, newNode)
        pHead2 = pHead2.next
    return pHead1

def hb(pHead1, pHead2):
    if pHead1 == None:
        return pHead2
    if pHead1.val <= pHead2.val:
        node = hb(pHead1.next, pHead2)
        pHead1.next = node
        return pHead1
    else:
        pHead2.next = pHead1
        return pHead2


if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(2)
    Node5 = ListNode(3)
    Node6 = ListNode(4)
    Node2.next = Node3
    Node1.next = Node2
    Node5.next = Node6
    Node4.next = Node5
    Merge(Node1, Node4)