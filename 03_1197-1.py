# 03 1197 최소 스패닝 트리 (구현: 01)
# 크루스칼 알고리즘
# 유니온 파인드

# 문제
# 그래프가 주어졌을 때, 
# 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

# 최소 스패닝 트리는, 
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 
# 그 가중치의 합이 최소인 트리를 말한다.

# 입력
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
# 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 
# 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

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