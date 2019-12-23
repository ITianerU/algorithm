"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if not nums or length < 3:
            return None
        min = nums[0] + nums[1] + nums[2] - target
        nums.sort()
        for index in range(length):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left = index + 1
            right = length - 1
            while left < right:
                result = nums[index] + nums[left] + nums[right] - target
                if result == 0:
                    min = result
                    break
                elif result < 0:
                    min = result if abs(result) < abs(min) else min
                    left = left + 1
                else:
                    min = result if abs(result) < abs(min) else min
                    right = right - 1
        return min + target