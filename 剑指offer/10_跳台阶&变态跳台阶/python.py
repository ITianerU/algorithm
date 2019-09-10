"""
#### 题目描述

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级... 它也可以跳上 n 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
"""
def jumpFloor(number):
    if number<=2:
        return number
    num = [0 for i in range(number)]
    num[0] = 1
    num[1] = 2
    for i in range(2,number):
        num[i] = num[i-1] + num[i-2]
    return num[number-1]


"""
#### 题目描述

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级... 它也可以跳上 n 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
台阶    跳法
 1       1
 2       2
 3       4
 4       8
"""
def jumpFloorII(number):
    if number<=2:
        return number
    num = [0 for i in range(number)]
    num[0] = 1
    num[1] = 2
    for i in range(2,number):
        num[i] = num[i-1] * 2
    return num[number-1]
