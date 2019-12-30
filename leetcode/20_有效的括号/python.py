"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses

"""

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            elif i == ')':
                if not l or l[len(l) - 1] != '(':
                    return False
                else:
                    l = l[:len(l) - 1]
            elif i == '}':
                if not l or l[len(l) - 1] != '{':
                    return False
                else:
                    l = l[:len(l) - 1]
            else:
                if not l or l[len(l) - 1] != '[':
                    return False
                else:
                    l = l[:len(l) - 1]
        if len(l) == 0:
            return True
        else:
            return False