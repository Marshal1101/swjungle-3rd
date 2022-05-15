## 16 2655 미로 만들기 (구현: 01)

# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 다익스트라

import sys
import heapq
from typing import get_args
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i].append(-1)
    graph[i] += list(map(int,input().strip()))

start, end = (0, 1, 1), (0, n, n)
distance = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def cost(x):
    if x == 1:
        return 0
    if x == 0:
        return 1

def dijkstra():
    q = []
    distance[1][1] = 0
    heapq.heappush(q, start)
    while q:
        c, i, j = heapq.heappop(q)
        if distance[i][j] < c:
            continue
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 1<= ni < n+1 and 1 <= nj < n+1:
                if c + cost(graph[ni][nj]) < distance[ni][nj]:
                    distance[ni][nj] = c + cost(graph[ni][nj])
                    heapq.heappush(q, (c + cost(graph[ni][nj]), ni, nj))
dijkstra()
print(distance[n][n])