## 23 1948 임계경로 ())
# 위상 정렬 사용

# 그래프 이론
# 그래프 탐색
# 위상 정렬

from collections import deque
import sys


input = sys.stdin.readline


n = int(input())
m = int(input())
indegree = [0] * (n+1)
time = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e, h = map(int,input().split())
    graph[s].append((e, h))
    indegree[e] += 1
start, end = map(int,input().split())

print(time)
print(graph)


def topology_sort(start) :
    result = []
    q = deque([start])
    time[start].append(0)
    while q :
        city = q.popleft()   
        result.append(city)
        for adj, hour in graph[city] :
            indegree[adj] -= 1
            for total_h in time[city] :
                time[adj].append(total_h + hour)
            if indegree[adj] == 0 :
                q.append(adj)

    for i in result :
        print(i, end=' ')
    print()
    for i in time :
        print(i, end=' ')
topology_sort(start)