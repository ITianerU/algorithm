"""
输入一个链表，输出该链表中倒数第k个结点。
#### 解题思路

设链表的长度为 N。设置两个指针 P1 和 P2，先让 P1 移动 K 个节点，则还有 N - K 个节点可以移动。此时让 P1 和 P2 同时移动，
可以知道当 P1 移动到链表结尾时，P2 移动到第 N - K 个节点处，该位置就是倒数第 K 个节点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findKthToTail(head, k):
    if head == None or k <= 0:
        return None
    count = 1
    p = head
    while head.next:
        if count != k:
            count = count + 1
        else:
            p = p.next
        head = head.next
    if count != k:
        return None
    return p

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node6.next = node7
    node5.next = node6
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    findKthToTail(node1, 2)