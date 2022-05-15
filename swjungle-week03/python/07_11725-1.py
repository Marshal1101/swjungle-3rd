## 07 11725 트리의 부모 찾기 (구현: 01)
## dfs 스택으로 만들어보기

import sys
input = sys.stdin.readline

n = int(input())
vertex = [[] for _ in range(n+1)]
for i in range(n-1):
    v1, v2 = map(int,input().split())
    vertex[v1].append(v2)
    vertex[v2].append(v1)

visited = [False] * (n+1)
parent = [0] * (n+1)

def dfs(vertex, start, visited, parent):
    stack = []
    stack.append(start)
    visited[start] = True
    while stack:
        node = stack.pop()
        for i in vertex[node]:
            if visited[i] != True:
                stack.append(i)
                visited[i] = True
                parent[i] = node

dfs(vertex, 1, visited, parent)
for j in range(2, n+1):
    print(parent[j])

