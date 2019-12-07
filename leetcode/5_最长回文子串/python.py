"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        if length == 0:
            return ""
        start, end = 0, 0
        # 遍历字符串, 每一次遍历的结果,都以它为回文数中心
        for index in range(length):
            # 回文数的中心为一个数字
            len1 = self.centerAroundLength(s, index, index)
            # 回文数的中心在两个相同数字之间
            len2 = self.centerAroundLength(s, index, index + 1)
            # 判断两次结果,哪个回文数比较长
            l = len1 if len1 > len2 else len2
            # 判断这次遍历的结果长度,是否比上次结果长
            if l > end - start:
                # 计算出回文数起始位置
                start = index - (l - 1) // 2
                end = index + l // 2
        return s[start: end+1]
    def centerAroundLength(self, s, start, end):
        # 判断start(回文数左边边界)是否大于0
        # 判断end(回文数右边边界)是否小于整个字符串长度
        # 判断回文数左边界的数与右边界的数是否相等
        while start >= 0 and end < len(s) and s[start] == s[end]:
            # 如果相等, 让左边界再往左移动一位, 右边界再往右移动一位
            start = start - 1
            end = end + 1
        # 返回回文数的长度
        # 减1的原因是, 最后一次遍历,start-1,end+1,需要-2, 但是-2会减掉回文数中心的长度,所以-1
        # 例子: 1223, 22是回文数,经过上面的循环后, start为0, end为3, 3-0-2 = 1 而22的长度2,所以减1即可
        return end - start - 1

