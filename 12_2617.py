## 12 2617 구슬 찾기 (구현: 01)
# DFS 사용

# 그래프 이론
# 그래프 탐색
# 깊이 우선 탐색
# 플로이드–와샬

from more_itertools import locate
import sys


input = sys.stdin.readline


n, m = map(int,input().split())
mid = n // 2
ascending =  [[] for i in list(range(n+1))]
descending = [[] for i in list(range(n+1))]

for _ in range(m):
    big, small = map(int,input().split())
    ascending[small].append(big)
    descending[big].append(small)


def DFS(start, graph):
    visited = [False] * (n+1)
    stack = [start]
    visited[start] = True

    count = 0
    while stack:
        num = stack.pop()
        for next in graph[num]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)
                count += 1
                if count > mid:
                    return 1

    return 0


under, over = 0, 0
for i in range(1, n+1):
    under += DFS(i, ascending)
    over += DFS(i, descending)
print(under + over)