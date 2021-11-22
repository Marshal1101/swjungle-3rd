## 20 2252 줄세우기 (구현: 01)

# 그래프 이론
# 위상 정렬

from collections import deque
import sys
from types import resolve_bases


input = sys.stdin.readline


# 노드 개수, 간선 개수
# 모든 노드의 진입차수 0으로 초기화
# 방향 그래프 모든 간선 정보 받기
# 방향성 따져서 화살표 받는 노드는 진입 차수 1증가
v, e = map(int,input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    start, end = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    # 처음 시작 시 진입차수가 0인 노드를 찾아서 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 꺼낼 때 그것이 곧 순서라서 결과에 보낸다.
        now = q.popleft()
        result.append(now)
        # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
