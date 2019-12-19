"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        # 取出数组中第一个字符串
        item = strs[0]
        # 遍历其他字符串
        for i in range(1, len(strs)):
            # 判断第一个字符串是否在 其他字符串中第一个位置
            while strs[i].find(item) != 0:
                # 如果没找到第一个字符串， 就截取第一个字符串， 保留1到长度-1位字符
                item = item[0: len(item) - 1]
                if not item:
                    return ""

        return item