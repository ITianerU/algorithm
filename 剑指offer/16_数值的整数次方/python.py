"""
#### 题目描述

给定一个 double 类型的浮点数 base 和 int 类型的整数 exponent，求 base 的 exponent 次方。

#### 解题思路

下面的讨论中 x 代表 base，n 代表 exponent。
"""

import math
def Power(base, exponent):
    # return math.pow(base, exponent)
    if exponent == 0:
        return 1
    m = base
    n = exponent
    if exponent < 0:
        exponent = -exponent
    for i in range(exponent-1):
        base = base * m
    if n < 0:
        base = 1 / base
    return base

def Power2(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    n = exponent
    if exponent < 0:
        exponent = -exponent
    if exponent % 2 == 0:
        base = Power2(base * base, exponent // 2)
    else:
        base = base * base * Power2(base, exponent // 2)
    if n < 0:
        return 1 / base
    return base

if __name__ == '__main__':
    print(Power(2, -2))
    print(Power2(2, -2))



