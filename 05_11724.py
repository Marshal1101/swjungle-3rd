## 05 11724 연결 요소의 개수 (구현: 01)
# BFS 사용

# 문제
# 방향 없는 그래프가 주어졌을 때,
# 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
edge = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

visited = [False] * (N+1)

def bfs(edge, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in edge[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True

count = 0
for j in range(1, N+1):
    if not visited[j]:
        bfs(edge, j, visited)
        count += 1

print(count)