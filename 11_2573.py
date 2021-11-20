## 11 2573 빙산 (메모리 초과)
# DFS 사용, 그런데 DFS는 힘들다고 함.

# 구현
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
world = []
for _ in range(n):
    world.append(list(map(int,input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
def dfs(matrix):
    global result
    stack = deque()
    variation = []
    visited = [[[False, 0] for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if matrix[i][j] != 0 and visited[i][j][0] == False:
                visited[i][j][0] = True
                stack.append([i, j])
                count += 1
                if count > 1:
                    return result
                while stack:
                    i, j = stack.pop()
                    vari = 0
                    for k in range(4):
                        ci = i + dx[k]
                        cy = j + dy[k]
                        if world[ci][cy] == 0:
                            vari += 1
                        else:
                            if visited[ci][cy][0] == False:
                                stack.append([ci, cy])
                                visited[ci][cy][0] = True
                    variation.append([i, j, vari])

    while variation:
        i, j, c = variation.pop()
        matrix[i][j] -= c
        if matrix[i][j] < 0:
            matrix[i][j] = 0
    result += 1
    dfs(matrix)

dfs(world)
print(result)