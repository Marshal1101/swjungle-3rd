## 15 1916 최소비용 구하기 (틀림, 왜?! 선형탐색이라서?)
# 선형탐색


# 그래프 이론
# 다익스트라


# 문제
# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

# 입력
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 
# 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2, c = map(int,input().split())
    graph[v1].append((v2, c)) 
start, end = map(int,input().split())
visited = [False] * (n+1)
min_cost = [float('inf')] * (n+1)

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = float('inf')
    index = 0
    for i in range(1, n+1):
        if min_cost[i] < min_value and not visited[i]:
            min_value = min_cost[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    min_cost[start] = 0
    visited[start] = True
    for adj in graph[start]:
        min_cost[adj[0]] = adj[1]
    # 시작 노드를 제외한 전체 n-1개의 노드 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리.
        # 방문처리는 이제 현재 노드(now)에서 다음 노드(ajac[0])까지 
        # 소요 되는 최단 거리(최소 비용)를 갱신할 거라는 뜻
        for adj in graph[now]:
            cost = min_cost[now] + adj[1]
            if cost < min_cost[adj[0]]:
                min_cost[adj[0]] = cost
            
# 다익스트라 알고리즘 수행
dijkstra(start)
print(min_cost[end])