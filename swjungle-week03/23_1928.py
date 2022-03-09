## 23 1948 임계경로 (틀림)
# 위상 정렬 사용
# BFS 사용

# 그래프 이론
# 그래프 탐색
# 위상 정렬

from collections import deque
import sys


input = sys.stdin.readline


n = int(input())
m = int(input())
indegree = [0] * (n+1)
time = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
re_graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m) :
    s, e, h = map(int,input().split())
    graph[s].append((e, h))
    re_graph[e].append((s, h))
    indegree[e] += 1
start, end = map(int,input().split())


def topology_sort(start) :
    result = []
    q = deque([start])
    while q :
        city = q.popleft()   
        result.append(city)
        for adj, hour in graph[city] :
            indegree[adj] -= 1
            time[adj] = max(time[adj], time[city] + hour)
            if indegree[adj] == 0 :
                q.append(adj)



def bfs(end) :
    load = 0
    q = deque()
    q.append(end)
    visited[end] = True
    while q :
        city = q.popleft()
        for adj, next_hour in re_graph[city] :
            if visited != True :
                visited[adj] = True
                if time[city] - time[adj] == next_hour :
                    load += 1 
                    q.append(adj)

    return load

topology_sort(start)
print(time[end])
print(bfs(end))