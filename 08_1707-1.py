## 08 1707 이분 그래프 (구현: 01)
# DFS 사용

import sys
input = sys.stdin.readline

# dfs
def dfs(start):
    stack = []
    visited[start] = 1 # 방문한 노드에 그룹번호 1 할당
    stack.append(start)
    while stack:
        node = stack.pop()
        for ajac in edge[node]:
            if visited[ajac] == -1: # 아직 안 가본 곳이면 방문
                visited[ajac] = 1 - visited[node]
                stack.append(ajac)
            elif visited[ajac] == visited[node]: # 방문한 곳인데, 그룹이 동일하면 False
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int,input().split())
    edge = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,input().split())
        edge[u].append(v)
        edge[v].append(u)

    visited = [-1] * (V+1)
    parent = [k for k in range(V+1)]
    root = [0 for _ in range(V+1)]
    for j in range(1, V+1):
        if visited[j] == -1:
            if dfs(j) == False:
                print('NO')
                break
    else:
        print('YES')