## 12 2617 구슬 찾기 (참조: 백준 빠른 풀이)
# DFS 사용

# 그래프 이론
# 그래프 탐색
# 깊이 우선 탐색
# 플로이드–와샬

import sys
def solve():
    n, m = map(int, sys.stdin.readline().strip().split())
    heavier = [[] * (n + 1) for _ in range(n + 1)]
    lighter = [[] * (n + 1) for _ in range(n + 1)]
    mid = n // 2

    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        heavier[v2].append(v1)
        lighter[v1].append(v2)

    def dfs(now, path):
        visited = [False] * (n + 1)
        stack = [now]
        visited[now] = True
        cnt = 0
        while stack:
            now = stack.pop()
            for next in path[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                    cnt += 1
                    if cnt > mid:
                        return 1
        return 0

    answer = 0
    for i in range(1, n + 1):
        answer += dfs(i, heavier)
        answer += dfs(i, lighter)
    return answer
print(solve())