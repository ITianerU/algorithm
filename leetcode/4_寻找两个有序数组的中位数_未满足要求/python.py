"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

"""
import math
class Solution(object):
    # 该解法时间复杂度为 O(m+n)
    def findMedianSortedArrays(self, nums1, nums2):
        temp = 0
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 == 0 and length2 == 0:
            return 0
        elif length1 == 0:
            temp = 1
        elif length2 == 0:
            temp = 2
        length = (length1 + length2) / 2
        index1, index2 = 0, 0
        result = 0
        for i in range(math.ceil(length)):
            if temp == 0:
                if nums1[index1] <= nums2[index2]:
                    result = nums1[index1]
                    index1 = index1 + 1
                    if index1 == length1:
                        temp = 1
                else:
                    result = nums2[index2]
                    index2 = index2 + 1
                    if index2 == length2:
                        temp = 2
            elif temp == 1:
                result = nums2[index2]
                index2 = index2 + 1
            else:
                result = nums1[index1]
                index1 = index1 + 1
        if (length1 + length2) % 2 == 0:
            if temp == 0:
                if nums1[index1] <= nums2[index2]:
                    result = (result + nums1[index1]) / 2
                else:
                    result = (result + nums2[index2]) / 2
            elif temp == 1:
                result = (result + nums2[index2]) / 2
            else:
                result = (result + nums1[index1]) / 2
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))