"""
#### 题目描述

输入一个整数，输出该数二进制表示中 1 的个数。

##### n&(n-1)

该位运算去除 n 的位级表示中最低的那一位。
"""

def NumberOf1(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n != 0:
        n = n & (n - 1)
        count = count + 1
    return count

if __name__ == '__main__':
    print(NumberOf1(10))

