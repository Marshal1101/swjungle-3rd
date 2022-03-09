## 13 2178 미로 탐색 (참조, 백준 빠른 풀이)
# DFS 사용

# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색

import sys
from sys import stdin
sys.setrecursionlimit(100000)

m, n = [int(x) for x in stdin.readline().split()]
maze = [[0]*n for i in range(m)]
visit = mat = [[0]*n for i in range(m)]
search = []

for i in range(m):
   str = stdin.readline()
   for j in range(n):
       maze[i][j] = int(str[j])


def find_maze():
    while len(search) > 0:
        x, y = search.pop(0)
        if x > 0 and maze[x-1][y] == 1:
            search.append((x - 1, y))
            maze[x - 1][y] = maze[x][y] + 1
        if x + 1 < m and maze[x + 1][y] == 1:
            search.append((x + 1, y))
            maze[x + 1][y] = maze[x][y] + 1
        if y > 0 and maze[x][y - 1] == 1:
            search.append((x, y - 1))
            maze[x][y - 1] = maze[x][y] + 1
        if y + 1 < n and maze[x][y + 1] == 1:
            search.append((x, y + 1))
            maze[x][y + 1] = maze[x][y] + 1


search.append((0, 0))
maze[0][0] = 1
find_maze()
print(maze[m-1][n-1])
