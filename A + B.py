"""
输入两个整数，求这两个整数的和是多少。
输入格式
输入两个整数A,B，用空格隔开，0≤A,B≤108
输出格式
输出一个整数，表示这两个数的和
样例输入：
3 4
样例输出：
7
"""
import sys

for line in sys.stdin:
    print(sum(map(int, line.split(" "))))