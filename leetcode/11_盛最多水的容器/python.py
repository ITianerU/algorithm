"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water

"""


class Solution:
    def maxArea(self, height):
        max = 0
        # 双指针一个指向开头，一个指向末尾，
        i = 0
        j = len(height) - 1
        # 比较两个指针指向的数据大小， 数据小的指针， 向两个指针中心靠一位
        while i != j:
            if height[i] < height[j]:
                max = height[i] * (j - i) if height[i] * (j - i) > max else max
                i = i + 1
            else:
                max = height[j] * (j - i) if height[j] * (j - i) > max else max
                j = j - 1
        return max