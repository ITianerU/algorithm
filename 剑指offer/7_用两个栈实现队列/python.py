"""
#### 题目描述

用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。

#### 解题思路

in 栈用来处理入栈（push）操作，out 栈用来处理出栈（pop）操作。一个元素进入 in 栈之后，出栈的顺序被反转。当元素要出栈时，需要先进入 out 栈，此时元素出栈顺序再一次被反转，因此出栈顺序就和最开始入栈顺序是相同的，先进入的元素先退出，这就是队列的顺序
"""

class Solution:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
    def push(self, node):
        # write code here
        self.stack1.append(node);
    def pop(self):
        # return xx
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop();

if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())
    s.push(5)
    print(s.pop())
    print(s.pop())



