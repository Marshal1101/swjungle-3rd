## 15 1916 최소비용 구하기 (구현: 01)

# 그래프 이론
# 다익스트라
# 우선순위 큐(최소 힙)

import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    v1, v2, c = map(int,input().split())
    graph[v1].append((v2, c)) 

start, end = map(int,input().split())
distance = [float('inf')] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 꺼냈는데 비용 값이 지금 최소 비용보다 크다? 아 그사이 갱신되었네. 꺼낸 거 스킵 
        if distance[now] < dist:
            continue
        for adj in graph[now]:
            cost = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))

dijkstra(start)
print(distance[end])