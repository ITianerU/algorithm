"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
"""
# import sys
#
# n, m, count = 0, 0, 0
# w = []
# v = []
# for index, line in enumerate(sys.stdin):
#     if index == 0:
#         n, m = map(int, line.split(" "))
#         w = [0 for i in range(n+1)]
#         v = [0 for i in range(n+1)]
#         count = n;
#     else:
#         w[index], v[index] = map(int, line.split(" "))
#         count = count - 1
#         if count == 0:
#             break
# h = [[0 for i in range(m+1)] for j in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if w[i] > j:
#             h[i][j] = h[i-1][j]
#         else:
#             h[i][j] = max(h[i-1][j], h[i-1][j-w[i]]+v[i])
# print(h[n][m])
n, w = map(int, input().split(" "))
wl = [0 for i in range(n+1)]
vl = [0 for i in range(n+1)]
for i in range(1, n+1):
    wl[i], vl[i] = map(int, input().split(" "))

result = [[0 for i in range(w+1)] for j in range(n+1)]
print(result)
for i in range(1, n+1):
    for j in range(1, w+1):
        if wl[i]>j:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-wl[i]]+vl[i])
print(result[n][w])
