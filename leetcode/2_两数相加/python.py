"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 递归解法
    def addTwoNumbers(self, l1, l2):
        a = 0
        b = 0
        count = 0
        while l1:
            a = a + l1.val * 10 ** count
            count = count + 1
            l1 = l1.next
        count = 0
        while l2:
            b = b + l2.val * 10 ** count
            count = count + 1
            l2 = l2.next
        sum = a + b
        if sum == 0:
            return ListNode(0)
        node = self.reserve(sum)
        return node

    def reserve(self, sum):
        if sum == 0:
            return
        node = ListNode(sum % 10)
        node.next = self.reserve(sum // 10)
        return node

if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(0)
    node2 = ListNode(0)
    s.addTwoNumbers(node1, node2)
