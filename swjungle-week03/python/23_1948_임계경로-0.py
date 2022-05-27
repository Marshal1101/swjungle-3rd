## 14	43858015	4	marshal1101	52476	288	Python 3 	1309

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
indegree = [0 for _ in range(N+1)]
max_time = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
re_graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M) :
    v1, v2, cost = map(int, input().split(' '))
    graph[v2].append([v1, cost])
    re_graph[v1].append([v2, cost])
    indegree[v1] += 1
start, end = map(int, input().split(' '))


def topology_sort(start, end) :
    q = deque([end])
    while q :
        cur_city = q.popleft()
        for adj, cost in graph[cur_city] :
            indegree[adj] -= 1
            max_time[adj] = max(max_time[adj], max_time[cur_city] + cost)
            if indegree[adj] == 0 :
                q.append(adj)
    return max_time[start]

def bfs(start) :
    cnt = 0
    q = deque([start])
    while q :
        cur_city = q.popleft()
        if visited[cur_city] != True :
            visited[cur_city] = True
            for adj, cost in re_graph[cur_city] :
                # print(max_time[cur_city], max_time[adj], cost)
                if (max_time[cur_city] - max_time[adj]) == cost :
                    q.append(adj)
                    cnt += 1
    return cnt

print(topology_sort(start, end))
print(bfs(start))