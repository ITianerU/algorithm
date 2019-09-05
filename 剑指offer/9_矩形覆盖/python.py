"""
#### 题目描述

我们可以用 2\*1 的小矩形横着或者竖着去覆盖更大的矩形。请问用 n 个 2\*1 的小矩形无重叠地覆盖一个 2\*n 的大矩形，总共有多少种方法？
#### 解题思路

当 n 为 1 时，只有一种覆盖方法：
当 n 为 2 时，有两种覆盖方法：
要覆盖 2\*n 的大矩形，可以先覆盖 2\*1 的矩形，再覆盖 2\*(n-1) 的矩形；或者先覆盖 2\*2 的矩形，再覆盖 2\*(n-2) 的矩形。而覆盖 2\*(n-1) 和 2\*(n-2) 的矩形可以看成子问题。该问题的递推公式如下：
f(n):  1    n=1
       2    n=2
       f(n-1)+f(n-2)   n>1
"""
def rectCover(number):
    if number <= 0:
        return number
    rects = [0 for i in range(number+1)]
    rects[0] = 1
    rects[1] = 2
    for i in range(2, number):
        rects[i] = rects[i-1] + rects[i-2]
    return rects[number-1]

if __name__ == '__main__':
    print(rectCover(1))