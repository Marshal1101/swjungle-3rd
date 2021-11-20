## 15 1916 최소비용 구하기 ()

# 그래프 이론
# 다익스트라

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edge = [ [] for _ in range(n+1) ]
for _ in range(m):
    v1, v2, c = map(int,input().split())
    edge[v1].append([v2, c])

start, end = map(int,input().split())
visited = [False] * (n+1)

def bfs(edge, start, end, visited):
    visited[start] = True
    
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for ajac in edge[node]:
            if visited[ajac[0]] == False:
                queue.append(ajac)
                visited[ajac[0]] = True
