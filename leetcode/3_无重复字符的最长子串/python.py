"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution(object):
    # 滑动窗口解法
    def lengthOfLongestSubstring(self, s):
        # max 最大长度, start 窗口的左边界, end 窗口的右边界
        max, start, end = 0, 0, 0
        # 创建一个滑动窗口(list), 该list存储的数据无重复,新数据从末尾加入,
        # 每当有重复的数据传入, 旧的重复数据和重复数据之前的数据清除
        l = list()
        for item in s:
            # 判断新数据是否重复
            if item in l:
                # 找到重复数据的位置, +1 为了方便下面使用切片
                index = l.index(item) + 1
                # 将滑动窗口中重复数据(包含重复数据之前的数据)通过切片,只保留不重复部分
                l = l[index:]
                # 修改左边界的位置
                start = start + index
            # 将新数据加入
            l.append(item)
            # 修改右边界位置
            end = end + 1
            # 通过右边界减左边界得出滑动窗口中数据的数量, 与目前的最大值比较, 进行替换
            max = max if max > end - start else end - start
        return max

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(" "))