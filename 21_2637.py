## 21 2637 장난감 조립 ()

# 그래프 이론
# 위상 정렬
# 다이나믹 프로그래밍

from collections import deque
import sys


input = sys.stdin.readline


v = int(input())
e = int(input())
dp = [{} for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
for _ in range(e):
    end, start, ea = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1
    dp[end][start] = ea
