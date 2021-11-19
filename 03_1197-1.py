# 03 1197 최소 스패닝 트리 (구현: 01)
# 크루스칼 알고리즘
# 유니온 파인드
from sys import stdin

# V: 정점 수, E: 간선 수, edge: 간선 리스트, w: 간선 가중치
input = stdin.readline
V, E = map(int, input().split())

edge = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    edge.append((w, v1, v2))


# 가중치를 기준으로 오름차순
edge.sort(key=lambda x: x[0])

# 부모 리스트 (인덱스를 정점으로 이용)
parent = list(range(V + 1))

# 결합: v1에 v2를 붙인다.
def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)

    if v1 == v2:
        return

    if v2 < v1:
        parent[v1] = v2
    else:
        parent[v2] = v1

# 부모 찾아가기, 본인이거나 조부모 이상일수도
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

# 가중치가 낮은 정점들부터 부모를 연결하여
# 부모가 최종 하나로 되면 최소 스패닝 트리
# 사이클 안 생김
weight = 0
for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        weight += w

print(weight)