"""
输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。

返回的结果用数组存储。

样例
输入：[2, 3, 5]
返回：[5, 3, 2]
"""

class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return head[::-1]

s = Solution()
print(s.printListReversingly([1,2,3]))