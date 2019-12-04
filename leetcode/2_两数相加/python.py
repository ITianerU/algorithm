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
    def addTwoNumbers2(self, l1, l2):
        # 进位,两数相加大于等于10 t=1, 小于10 t=0
        t = 0
        # 使用两个指针指向同一个对象
        node = ListNode(0)
        node2 = node
        while l1 or l2:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            sum = t + a + b
            t = 1 if sum >= 10 else 0
            sum = sum % 10
            # node指针始终指向链表最后一个元素, node2指向链表头
            node.next = ListNode(sum)
            node = node.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        # t大于0进位
        if t > 0:
            node.next = ListNode(1)
        return node2.next


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
    s.addTwoNumbers2(node1, node2)
