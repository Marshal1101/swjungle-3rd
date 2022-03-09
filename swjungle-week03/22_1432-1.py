## 22 1432 그래프 수정 (참조, https://always-be-wise.tistory.com/62)
# 위상 정렬 사용

# 그래프 이론
# 플로이드–와샬
# 위상 정렬

import sys, heapq

def topology_sort(N):
    queue = []
    # 정점의 수만큼 아래 과정을 반복한다.
    for num in range(1, N + 1):
        # 만약 차수가 0이면
        if degree[num] == 0:
            # 우선 순위 큐에 넣어준다.
            # 대신 나중에 사전 순으로 출력하기 위해 숫자를 음수 취한다. 
            heapq.heappush(queue,-num)

    while queue:
        now = -heapq.heappop(queue)
        # 처음 힙에서 뽑는 것은 그 어느 숫자보다 큰 것이기에
        # 해당 숫자를 인덱스로 하는 result 리스트에 전체 개수인 N을 할당한다.
        result[now] = N

        # 그 다음으로 큰 숫자를 찾기 위해 아래의 과정을 진행한다.
        for adj_num in graph[now]:
            degree[adj_num] -= 1
            if degree[adj_num] == 0:
                heapq.heappush(queue,-adj_num)
        N -= 1


# 전체 정점의 개수를 입력받는다.
N = int(sys.stdin.readline().rstrip())

# 차수 리스트를 만든다.
degree = [0] * (N + 1)

# 결과를 담을 리스트를 만든다.
result = [0] * (N + 1)

# 정점의 관계를 담을 그래프를 만든다.
graph = [[] for _ in range(N + 1)]
for num in range(1, N + 1):
    info = list(map(int,sys.stdin.readline().strip()))
    # print(info)
    
    # 입력 받은 값을 graph에 넣어 줄때, 
    # 정점의 위치 정보가 1부터 시작한다는 것을 고려하여 idx를 변화시키고 차수도 늘려준다.
    for idx, value in enumerate(info):
        # print(idx, value)
        if value == 1:
            graph[idx+1].append(num)
            degree[num] +=1

# print(graph)
# print(degree)

topology_sort(N)

if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])