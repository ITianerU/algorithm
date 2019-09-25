"""
#### 题目描述

地上有一个 m 行和 n 列的方格。一个机器人从坐标 (0, 0) 的格子开始移动，每一次只能向左右上下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 k 的格子。

例如，当 k 为 18 时，机器人能够进入方格 (35,37)，因为 3+5+3+7=18。但是，它不能进入方格 (35,38)，因为 3+5+3+8=19。请问该机器人能够达到多少个格子？

#### 解题思路

使用深度优先搜索（Depth First Search，DFS）方法进行求解。回溯是深度优先搜索的一种特例，它在一次搜索过程中需要设置一些本次搜索过程的局部状态，并在本次搜索结束之后清除状态。而普通的深度优先搜索并不需要使用这些局部状态，虽然还是有可能设置一些全局状态
"""

from functools import reduce
next = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def movingCount(threshold, rows, cols):
    count = 0
    marked = [[None for i in range(cols)] for j in range(rows)]
    marked = backtracking(threshold,marked, 0, 0, rows, cols)
    for i in marked:
        for j in i:
            if j == True:
                count = count + 1
    return count


def backtracking(threshold, marked, row, col, rows, cols):
    if row<0 or row>=rows or col<0 or col>=cols or marked[row][col]:
        return marked
    if sum(map(int, list(str(row)))) + sum(map(int, list(str(col)))) > threshold:
        return marked
    marked[row][col] = True
    for item in next:
        marked = backtracking(threshold, marked, row+item[0], col+item[1], rows, cols)
    return marked


if __name__ == '__main__':
    print(movingCount(15,20,20))



