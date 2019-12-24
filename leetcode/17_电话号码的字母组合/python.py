"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""
from typing import List


class Solution:
    # 递归
    def letterCombinations(self, digits: str) -> List[str]:
        d = dict()
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        output = []
        if digits:
            self.backtrack("", digits, output, d)
        return output
    # combination: 每次递归分支的字符串， next_digits: 剩余的号码
    def backtrack(self, combination, next_digits, output, phone):
        # 递归结束条件， 当没有剩余号码时， 将递归的分支字符串存入结果集
        if len(next_digits) == 0:
            output.append(combination)
        else:
            # 当有剩余号码， 提取出第一个号码， 从字典中取出该号码对应的字母列表， 并遍历
            for letter in phone[next_digits[0]]:
                # 遍历的每一个结果，都进行递归， 将当前节点的字符与遍历的字符想加 和 剩余号码去除第一位作为参数， 传入
                self.backtrack(combination + letter, next_digits[1:], output, phone)

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("233"))
