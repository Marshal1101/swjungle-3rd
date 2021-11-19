## 04 1260 DFS와 BFS (구현: 01)

from collections import deque
import sys
input = sys.stdin.readline

# 자료구조 - 인접리스트
N, M, V = map(int,input().split())
ajacent = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int,input().split())
    ajacent[v1].append(v2)
    ajacent[v2].append(v1)

# 방문 시 작은 수 먼저 방문하므로, 인접정점 오름차순 정렬
for i in range(N+1):
    ajacent[i].sort()


# 자료구조 - 방문리스트
visited = [False] * (N+1)

# DFS
def dfs(ajacent, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in ajacent[v]:
        if visited[i] != True:
            dfs(ajacent, i, visited)

# BFS
def bfs(ajacent, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in ajacent[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True

dfs(ajacent, V, visited)
print()
visited = [False] * (N+1)
bfs(ajacent, V, visited)