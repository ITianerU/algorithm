"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplication(listNode):
    if not listNode or not listNode.next:
        return listNode
    next = listNode.next
    if listNode.val == next.val:
        while next != None and listNode.val == next.val:
            next = next.next
        return deleteDuplication(next)
    else:
        listNode.next = deleteDuplication(next)
        return listNode

if __name__ == '__main__':
    listNode1 = ListNode(1)
    listNode2 = ListNode(2)
    listNode3 = ListNode(2)
    listNode4 = ListNode(3)
    listNode5 = ListNode(4)
    listNode4.next = listNode5
    listNode3.next = listNode4
    listNode2.next = listNode3
    listNode1.next = listNode2
    deleteDuplication(listNode1)
