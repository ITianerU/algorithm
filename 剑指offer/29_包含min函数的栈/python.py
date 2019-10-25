"""
#### 题目描述

题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
"""

# -*- coding:utf-8 -*-

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.minList = list()
        self.sortList = list()
    def push(self, node):
        self.sortList.append(node)
        if self.minList.__len__() == 0:
            self.minList.append(node)
        else:
            for index, item in enumerate(self.minList):
                if node < item:
                    self.minList.insert(index, node)
                    return
            self.minList.append(node)

    def pop(self):
        node = self.sortList.pop(len(self.sortList)-1)
        self.minList.remove(node)
        return node
    def top(self):
        return self.sortList[len(self.sortList)-1]
    def min(self):
        return self.minList[0]


if __name__ == '__main__':
    test = Solution()
    test.push(3)
    print(test.min())
    test.push(4)
    print(test.min())
    test.push(2)
    print(test.min())
    test.push(3)
    print(test.min())
    print(test.pop())
    print(test.min())
    print(test.pop())
    print(test.min())
    print(test.pop())
    print(test.min())
    test.push(0)
    print(test.min())
