"""
输入一个链表，反转链表后，输出新链表的表头。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    if pHead == None or pHead.next == None:
        return pHead
    next = pHead.next
    pHead.next = None
    newHead = ReverseList(next)
    next.next = pHead
    return newHead

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node2.next = node3
    node1.next = node2
    ReverseList(node1)