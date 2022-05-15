## 14 18352 특정 거리의 도시 찾기 (참조, 백준 빠른 풀이)

import heapq
import sys
read = sys.stdin.readline


def solve():
    N, M, K, X = map(int, read().split())
    # 인접 리스트
    adj = [list() for _ in range(N+1)]
    for _ in range(M):
        f, t = map(int, read().split())
        adj[f].append(t)

    # 최단 거리 배열
    min_dists = [300002] * (N+1)

    # 우선순위 큐
    # (해당 노드까지의 최단거리, 노드번호) 튜플을 원소로 가짐
    q = []
    heapq.heappush(q, (0, X))
    min_dists[X] = 0

    ans = []

    # 남은 모든 노드들에 대하여
    while q:
        # 우선순위 큐 안에 있는 최단 거리 노드 선택
        dist, node = heapq.heappop(q)
        # 이미 처리된 노드라면 continue
        if min_dists[node] < dist:
            continue

        # 현재 노드까지의 거리가 K라면 정답 리스트에 저장 후 continue
        if min_dists[node] == K:
            ans.append(str(node))
            continue

        # 연결된 노드들의 최단거리 갱신 후 우선순위 큐에 추가
        for to in adj[node]:
            if min_dists[to] > dist + 1:
                min_dists[to] = dist + 1
                heapq.heappush(q, (dist+1, to))

    return '\n'.join(ans) if ans else -1


print(solve())