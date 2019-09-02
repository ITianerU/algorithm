"""
#### 题目描述

从尾到头反过来打印出每个结点的值。
#### 解题思路

##### 使用递归

要逆序打印链表 1->2->3（3,2,1)，可以先逆序打印链表 2->3(3,2)，最后再打印第一个节点 1。而链表 2->3 可以看成一个新的链表，要逆序打印该链表可以继续使用求解函数，也就是在求解函数中调用自己，这就是递归函数。
"""
class listNode():
    def __init__(self, x):
        self.value = x
        self.next = None

def printListFromTailToHead1(listNode):
    nlist = list()
    if listNode != None:
        nlist.extend(printListFromTailToHead1(listNode.next))
        nlist.append(listNode.value)
    return nlist

"""
结点和第一个节点的区别：

- 头结点是在头插法中使用的一个额外节点，这个节点不存储值；
- 第一个节点就是链表的第一个真正存储值的节点。
"""

def printListFromTailToHead2(lNode):
    head = listNode(-1)
    while lNode != None:
        nextNode = lNode.next
        lNode.next = head.next
        head.next = lNode
        lNode = nextNode

    nlist = list()
    head = head.next
    while head != None:
        nlist.append(head.value)
        head = head.next

    return nlist

"""
使用栈

栈具有后进先出的特点，在遍历链表时将值按顺序放入栈中，最后出栈的顺序即为逆序。
"""
# def printListFromTailToHead3(lNode):
#     nlist = list()
#     while lNode != None:
#         nlist.append(lNode.value)
#         lNode = lNode.next
#
#     nlist2 = list()
#     while len(nlist)>0:
#         nlist2.append(nlist.pop())
#
#     return nlist2



if __name__ == '__main__':
    L1 = listNode(1)
    L2 = listNode(2)
    L3 = listNode(3)
    L4 = listNode(4)
    L5 = listNode(5)
    L4.next = L5
    L3.next = L4
    L2.next = L3
    L1.next = L2
    # print(printListFromTailToHead3(L1))
    print(printListFromTailToHead1(L1))
    print(printListFromTailToHead2(L1))