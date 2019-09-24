"""
#### 题目描述

判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向上下左右移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

例如下面的矩阵包含了一条 bfce 路径。
#### 解题思路

使用回溯法（backtracking）进行求解，它是一种暴力搜索方法，
通过搜索所有可能的结果来求解问题。回溯法在一次搜索结束时需要进行回溯（回退），
将这一次搜索过程中设置的状态进行清除，从而开始一次新的搜索过程。例如下图示例中，
从 f 开始，下一步有 4 种搜索可能，如果先搜索 b，需要将 b 标记为已经使用，防止重复使用。
在这一次搜索结束之后，需要将 b 的已经使用状态清除，并搜索 c。
"""

next = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def hasPath(matrix, rows, cols, path):
    if rows == 0 or cols == 0:
        return False
    matrixList = list()
    matrix = list(matrix)
    for i in range(rows):
        matrixListIn = list()
        for j in range(cols):
            matrixListIn.append(matrix.pop())
        matrixList.append(matrixListIn)
    marked = [[ None for i in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if backtracking(matrixList, path, marked, 0, i, j,rows,cols):
                return True
    return False

def backtracking(matrixList, path, marked, pathLen, row, col, rows, cols):
    if len(path) == pathLen:
        return True
    if row<0 or row>=rows or col<0 or col>=cols or matrixList[row][col] != path[pathLen] or marked[row][col]:
        return  False
    marked[row][col] = True
    for i in next:
        if backtracking(matrixList, path, marked, pathLen+1, row+i[0], col+i[1],rows,cols):
            return True
    marked[row][col] = False
    return False

if __name__ == '__main__':
    print(hasPath("ABCESFCSADEE",3,4,"ABCCED"))
