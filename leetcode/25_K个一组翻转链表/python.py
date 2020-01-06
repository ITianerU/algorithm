"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        # 创建两个头指针, result始终指向头节点, temp随着遍历不断向末尾指
        result = temp = ListNode(0)
        while True:
            count = k
            # 创建栈
            stack = []
            # 临时头节点
            tmp = head
            # 往栈中添加头节点
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 当count不为0时, 说明上面的节点数量不足k个, 跳出循环
            if count:
                temp.next = head
                break
            # 翻转操作
            while stack:
                temp.next = stack.pop()
                temp = temp.next
            # 与剩下链表连接起来
            temp.next = tmp
            head = tmp
        return result.next