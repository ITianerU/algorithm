"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix == None:
            return None
        ylen = len(matrix)
        xlen = len(matrix[0])
        x = 0
        y = 0
        m = 0
        n = 0
        i = 0
        isLeftToRight = True
        isRightToLeft = False
        isUpToDown = False
        isDownToUp = False
        count = xlen * ylen
        result = list()
        while i < count:
            if x >= m and y >= n and x < xlen and y < ylen:
                if isLeftToRight:
                    result.append(matrix[y][x])
                    x = x + 1
                    i = i + 1
                elif isUpToDown:
                    result.append(matrix[y][x])
                    y = y + 1
                    i = i + 1
                elif isRightToLeft:
                    result.append(matrix[y][x])
                    x = x - 1
                    i = i + 1
                elif isDownToUp:
                    result.append(matrix[y][x])
                    y = y - 1
                    i = i + 1
            elif x == xlen:
                isLeftToRight = False
                isUpToDown = True
                x = x - 1
                y = y + 1
                n = n + 1
            elif y == ylen:
                isUpToDown = False
                isRightToLeft = True
                y = y - 1
                x = x - 1
                xlen = xlen - 1
            elif x < m:
                isRightToLeft = False
                isDownToUp = True
                x = x + 1
                y = y - 1
                ylen = ylen - 1
            elif y < n:
                isDownToUp = False
                isLeftToRight = True
                y = y + 1
                x = x + 1
                m = m + 1
        return result

if __name__ == '__main__':
    array = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    # array = [[1]]
    test = Solution()
    print(test.printMatrix(array))
