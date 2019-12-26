"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        count = len(nums)
        result = []
        if not nums or count < 4:
            return result
        nums.sort()
        for k in range(count - 3):
            # 判断是否与上一个数相等, 若相等, 跳过当次循环
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # 获取当前的最小值, 因为排过序, 所以最前面的四个数之和最小
            if nums[k] + nums[k+1] + nums[k+2] + nums[k+3] > target:
                break
            # 获取当前最大值
            if nums[k] + nums[count-1] + nums[count-2] + nums[count-3] < target:
                break
            # 第二层循环, 将后面的部分转换为三数之和等于 target-nums[k]
            for i in range(k+1,count-2):
                if i > k + 1 and nums[i] == nums[i-1]:
                    continue
                j = i + 1
                e = count - 1
                # 获取最小值, 进行比较
                if nums[i] + nums[j] + nums[j+1] >  target - nums[k]:
                    continue
                # 获取最大值, 进行比较
                if nums[i] + nums[e-1] + nums[e] < target - nums[k]:
                    continue
                while j < e:
                    sum = nums[k] + nums[i] + nums[j] + nums[e]
                    if sum == target:
                        result.append([nums[k], nums[i], nums[j], nums[e]])
                        j += 1
                        while j < e and nums[j] == nums[j-1]:
                            j += 1
                        e -= 1
                        while j < e and i < e and nums[e] == nums[e+1]:
                            e -= 1
                    elif sum < target:
                        j += 1
                        while j < e and nums[j] == nums[j-1]:
                            j += 1
                    else:
                        e -= 1
                        while j < 3 and nums[e] == nums[e+1]:
                            e -= 1
        return result