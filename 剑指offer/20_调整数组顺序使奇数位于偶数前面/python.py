"""
#### 题目描述

需要保证奇数和奇数，偶数和偶数之间的相对位置不变
"""

def reOrderArray(array):
    even = list()
    odd = list()
    for item in array:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return odd + even

if __name__ == '__main__':
    print(reOrderArray([1,2,3,4,5]))
