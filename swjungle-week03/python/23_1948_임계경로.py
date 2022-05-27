## 비트 쉬프트 시도

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
indegree = [0 for _ in range(N+1)]
max_time = [[0, None] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for i in range(M) :
    v1, v2, cost = map(int, input().split(' '))
    graph[v2].append([v1, cost])
    indegree[v1] += 1
print('N, M', N, M)
print('indegree', indegree)
print('max_time', max_time)
print('graph', graph)
start, end = map(int, input().split(' '))


q = deque([[end, 0, 0]])
while q :
    cur_city, paid, path = q.popleft()
    path = path | 1 << cur_city
    for adj, cost in graph[cur_city] :
        exp_paid = paid + cost
        indegree[adj] -= 1
        if exp_paid > max_time[adj][0] :
            max_time[adj][0] = exp_paid
            max_time[adj][1] = path
        if indegree[adj] == 0 :
            q.append([adj, max_time[adj][0], max_time[adj][1]])
    
print('time path', max_time)
print('maxtime', max_time[1][0])
print('maxpathcnt', bin(max_time[1][1]))
print(bin(196))
print(bin(192))