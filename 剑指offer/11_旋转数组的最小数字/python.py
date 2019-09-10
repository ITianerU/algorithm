"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
解题思路
将旋转数组对半分可以得到一个包含最小元素的新旋转数组，以及一个非递减排序的数组。新的旋转数组的数组元素是原数组的一半，从而将问题规模减少了一半，这种折半性质的算法的时间复杂度为 O(logN)（为了方便，这里将 log<sub>2</sub>N 写为 logN）
"""
def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    while len(rotateArray) > 2:
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        count = len(rotateArray)//2
        left = rotateArray[:count]
        right = rotateArray[count:]
        if bj(left):
            rotateArray = left
        else:
            rotateArray = right
    return rotateArray[0] if rotateArray[0]<=rotateArray[-1] else rotateArray[-1]


def bj(rotateArray):
    index = 0
    while len(rotateArray) > 1:
        if rotateArray[index] > rotateArray[-(index+1)]:
            return True
        elif rotateArray[index] == rotateArray[-(index+1)]:
            if index>= len(rotateArray)//2:
                return False
            index = index + 1
        else:
            return False
    return False
if __name__ == '__main__':
    print(minNumberInRotateArray([3,3,3,4,5,6,1,1,2,2]))