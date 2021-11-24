## 23 1948 임계경로 (참조, https://always-be-wise.tistory.com/63)
# 위상 정렬 사용
# BFS 사용

# 그래프 이론
# 그래프 탐색
# 위상 정렬


import sys
from collections import deque

# 도시의 수
num_of_city = int(sys.stdin.readline().rstrip())

# 도로의 수
num_of_road = int(sys.stdin.readline().rstrip())

# 주어진 정보를 바탕으로 전진 방향과 후진 방향 그래프를 만든다.
# 차수는 전진 방향 기준으로 작성한다.
foward_tracking = [[] * (num_of_city + 1) for _ in range(num_of_city + 1)]
back_tracking = [[] * (num_of_city + 1) for _ in range(num_of_city + 1)]
degree = [0] * (num_of_city + 1)

for _ in range(num_of_road):
    city_A, city_B, time = map(int, sys.stdin.readline().split())
    foward_tracking[city_A].append((city_B, time))
    back_tracking[city_B].append((city_A, time))
    degree[city_B] += 1

print(foward_tracking)
print(back_tracking)

# 출발 도시와 도착 도시를 입력 받는다.
start_city, end_city = map(int, sys.stdin.readline().split())

# 출발 도시로부터 도시 별 도착 시간을 담을 리스트를 만든다.
result = [0] * (num_of_city + 1)

# 방문 여부를 확인할 리스트를 만든다.
visited = [0] * (num_of_city + 1)


queue = deque()
queue.append(start_city)

def topology_sort():
    while queue:
        current_city = queue.popleft()
        # 현재 도시(시작 도시)의 인접 도시(adj_city)와 해당 인접 도시까지 가는데 걸리는 시간(time)을 확인한다.
        for adj_city, time in foward_tracking[current_city]:
            # 현재 도시에서 인접 도시까지 가는데 걸리는 시간을 초기 값에서 변경한다.
            result[adj_city] = max(result[adj_city], result[current_city] + time)
            # 인접 도시의 진입 차수를 줄인다.
            degree[adj_city] -= 1

            # 만약 인접 도시의 차수가 0이 되면 queue에 넣는다.
            if degree[adj_city] == 0:
                queue.append(adj_city)
            
    # 이런 식으로 queue에 담기는 도시가 없을 때까지 쭉 돌면 
    # 시작 도시에서 각 도시 별로 이동할 때 걸리는 시간을 담은 리스트(result)가 완성된다.
    print(result)

    count_city = 0
    queue.append(end_city)
    # 이제 도착 도시부터 되돌아 오는 과정을 갖는다.
    while queue:
        current_city = queue.popleft()
        # 현재 도시(도착 도시)의 인접 도시(adj_city)와 해당 인접 도시까지 가는데 걸리는 시간(time)을 확인한다.
        for adj_city, time in back_tracking[current_city]:
            # 현재 도시까지 오는데 걸리는 시간에서 인접 도시까지 걸리는 시간을 뺀 값이
            # 인접 도시에서 현재 도시까지 오는 시간과 같다면
            if result[current_city] - result[adj_city] == time:
                print(f'current_city는 {current_city}, adj_city는 {adj_city}')
                # 그 도시는 경로에 포함된 도시이다.
                count_city += 1
                # 그 도시에 대해 방문 표시가 0이라면
                if visited[adj_city] == 0:
                    # 방문 표시를 해주고
                    visited[adj_city] = 1
                    print(f'넘어온 adj_city는 {adj_city}')
                    # queue에 넣어준다.
                    queue.append(adj_city)
                    print(adj_city)

    print(result[end_city])
    print(count_city)

topology_sort()