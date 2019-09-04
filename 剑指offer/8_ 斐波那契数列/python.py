"""
#### 题目描述

求斐波那契数列的第 n 项，n <= 39。
0  n=0
1  n=1
f(n-1)+f(n-2)  n>1
#### 解题思路

如果使用递归求解，会重复计算一些子问题。例如，计算 f(4) 需要计算 f(3) 和 f(2)，计算 f(3) 需要计算 f(2) 和 f(1)，可以看到 f(2) 被重复计算了。
"""
def fibonacci(n):
    if n<=0:
        return n;
    nlist = [0 for i in range(n+1) ]
    nlist[0] = 0
    nlist[1] = 1
    for i in range(2, n+1):
        nlist[i] = nlist[i-1] + nlist[i-2]
    return nlist[n]

if __name__ == '__main__':
    print(fibonacci(40))

