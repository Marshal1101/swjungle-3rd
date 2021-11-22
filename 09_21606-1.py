## 09 21606 아침 산책(참조, https://always-be-wise.tistory.com/54)


import sys
sys.setrecursionlimit(100000)

# 전체 정점의 수
num_of_vertex = int(sys.stdin.readline().rstrip())

# 정점 별 실내(1)/실외(0) 정보, 인덱싱을 위해서 맨 앞에 0 추가한다.
vertex_info = [0] + list(map(int, sys.stdin.readline().rstrip()))

# 정점들을 연결한 그래프
vertex_graph = [[] for _ in range(num_of_vertex + 1)]

# 전체 간선의 수는 전체 정점의 수 -1
for _ in range(num_of_vertex-1):
    vertex_1, vertex_2 = map(int, input().split())
    vertex_graph[vertex_1].append(vertex_2)
    vertex_graph[vertex_2].append(vertex_1)

# 실외인 정점이 들어왔을 때 인접한 정점들을 계산헤야 한다.
def DFS(vertex_0):
    count = 0
    # 실외인 정점의 인접 정점을 하나씩 확인하면서
    for adj_vertex in vertex_graph[vertex_0]:
        # 인접 정점이 실내라면, 경로의 수를 추가해주고
        if vertex_info[adj_vertex] == 1:
            count += 1
        # 실내가 아닌 경우,
        else :
            # 아직 방문하지 않은 정점이었다면
            if adj_vertex not in visited:
                # 해당 정점에 대해서 다시 DFS를 하여 경로의 수를 추가한다.
                visited.add(adj_vertex)
                count += DFS(adj_vertex)
    return count


# 전체 경로의 수
total_count = 0

# 단순 경로임을 고려하여 정점들의 방문 여부를 set으로 표현한다.
visited = set()

# 정점의 수만큼 아래 과정을 반복한다.
for i in range(1, num_of_vertex + 1):
    # 정점이 실내라면
    if vertex_info[i] == 1:
        # 해당 실내 정점과 인접한 정점을 살펴본다.
        for adj_vetex in vertex_graph[i]:
            # 인접한 정점이 실내라면 바로 경로의 수를 추가한다.
            if vertex_info[adj_vetex] == 1:
                total_count += 1
    # 정점이 실외라면
    else:
        # 그리고 해당 실외 정점을 아직 방문하지 않았다면
        if i not in visited:
            # 방문 여부를 추가해주고
            visited.add(i)
            # 해당 실외 정점에 대해서 DFS를 실행한다.
            temp = DFS(i)
            # 실외 정점 기준으로 주변에 실내 정점이 몇 개있는지를 계산해주어야 한다.
            # 이 과정은 아래와 같은 점화식으로 표현할 수 있다.
            total_count += temp * (temp -1)

print(total_count)