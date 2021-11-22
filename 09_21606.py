## 09 21606 아침 산책 (73점)
# DFS 사용
# 1 ~ N개 정점에서 i 와 i+1 사이에 모두 간선 있을 때 뭔가 문제발생???

# 수학
# 그래프 이론
# 그래프 탐색
# 트리
# 깊이 우선 탐색
# 조합론


import sys
input = sys.stdin.readline

n = int(input())

inside = []
inside.append('실내1, 아외0')
inside += list(map(int,input().strip()))

edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

def dfs(start):
    if inside[start] == 0:
        return 0
    visited = [False] * (n+1) 
    stack = []
    count = 0
    visited[start] = True
    stack.append(start)
    while stack:
        node = stack.pop()
        for adj in edge[node]:
            if visited[adj] == False:
                if inside[adj] == 1:
                    count += 1
                else:
                    visited[adj] = True
                    stack.append(adj)
                
    return count


total = 0
for i in range(1, n+1):
    total = total + dfs(i)
print(total)