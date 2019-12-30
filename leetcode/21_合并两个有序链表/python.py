"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        end = result
        while l1 or l2:
            # print(result)
            if not l1 and l2:
                end.next = ListNode(l2.val)
                l2 = l2.next
                end = end.next
            elif not l2 and l1:
                end.next = ListNode(l1.val)
                l1 = l1.next
                end = end.next
            elif l1.val < l2.val:
                end.next = ListNode(l1.val)
                l1 = l1.next
                end = end.next
            else:
                end.next = ListNode(l2.val)
                l2 = l2.next
                end = end.next
        return result.next