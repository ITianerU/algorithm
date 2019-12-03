"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""

class Solution:
    # 该方案超出内存限制
    def twoSum(self, nums, target):
        length = len(nums)
        numList = list()
        for i in range(length):
            for j in range(length):
                numList.append(nums[i] + nums[j])

        for index, item in enumerate(numList):
            if item == target:
                y = index % length
                x = index // length
                if x == y:
                    continue
                return [x, y]
        return None

    def twoSum2(self, nums, target):
        length = len(nums)
        for i in range(length):
            y = target - nums[i]
            for j in range(i+1, length):
                if y == nums[j]:
                    return [i, j]
        return None

    # 哈希表解法
    def twoSum3(self, nums, target):
        d = dict()
        for index, num in enumerate(nums):
            d[num] = index
        length = len(nums)
        for i in range(length):
            y = target - nums[i]
            for k, v in d.items():
                if k == y and v != i:
                    return [i, v]
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum3([2, 7, 11, 15], 9))
