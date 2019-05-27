"""
给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。

请找出数组中任意一个重复的数，但不能修改输入的数组。

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
思考题：如果只能使用 O(1) 的额外空间，该怎么做呢？
"""
import sys

class Solution(object):
    def duplicateInArray(self, nums):
        length = len(nums)
        for index, num in enumerate(nums):
            for j in range(index + 1, length):
                if num == nums[j]:
                    return num
        return -1

solution = Solution()
print(solution.duplicateInArray([2, 3, 5, 4, 3, 2, 6, 7]))