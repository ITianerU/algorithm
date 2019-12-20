"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = len(nums)
        if not nums or count < 3:
            return []
        # 先排序
        nums.sort()
        result = []
        # 遍历排序后的数组， i表示3个数字的第一个数
        for i in range(count):
            # 因为数组是排序的， 所以当第一个数字大于0时， 三数想加不可能等于0
            if nums[i] > 0:
                return result
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left表示第二个数字， 从i后面第一位开始
            left = i + 1
            # right表示第三位数字， 从最后一位开始
            right = count - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    # 跳过重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while right > left and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return result