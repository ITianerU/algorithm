"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 递归
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # 获取第二个节点
        temp = head.next
        # 将第三个节点参与递归
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp
