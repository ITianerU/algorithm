"""
题目描述
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。请找出数组中任意一个重复的数字。

Input:
{2, 3, 1, 0, 2, 5}

Output:
2
"""


def duplicate(numbers, duplication):
    if numbers == None or len(numbers) < 0:
        return False
    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                print(numbers[i])
                return True
            swap(numbers, i, numbers[i])

    return False

def swap(numbers, i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp


if __name__ == '__main__':
    duplicate([10,8,3,1,9,10,7,4,6,7,2], None)
