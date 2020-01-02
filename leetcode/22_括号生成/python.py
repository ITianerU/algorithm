"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.recursion('', 0, 0, n, result)
        return result

    def recursion(self, s, left, right, n, result):
        # 表示字符串长度满足, n的2倍
        if len(s) == 2 * n:
            result.append(s)
            return
        # 当左括号的数量 < n时, 递归, 添加左括号, 左括号(left)数量加一
        if left < n:
            self.recursion(s + "(", left+1, right, n, result)
        # 当右括号的数量 < 左括号的数量, 递归, 添加右括号, 右括号(right)数量加一
        if right < left:
            self.recursion(s + ")", left, right+1, n, result)