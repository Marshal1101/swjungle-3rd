## 21 2637 장난감 조립 (참조, https://always-be-wise.tistory.com/62?category=1019502)
# 위상 정렬 사용

# 그래프 이론
# 위상 정렬
# 다이나믹 프로그래밍
<<<<<<< HEAD
import sys
from collections import deque

# N : 완제품의 번호
N = int(sys.stdin.readline().rstrip())

# M : 부품 조합 정보 개수
M = int(sys.stdin.readline().rstrip())

# 부품 조합 정보를 담을 리스트를 만든다.
assembly_info = [[] for _ in range(N + 1)]

# 제품 별로 얼마나 필요로 되는 지를 확인할 수 있는 리스트를 만든다.
# 위상 정렬의 진입 차수라고 생각하면 된다.
part_info = [0] * (N + 1)

# 부품 조합 정보를 입력받아 assembly_info에 넣어준다.
# 정보를 넣어주고 assembly_info[7]을 확인하면
# 7번 product를 만드는데 필요한 부품인 part와 그 수를 알 수 있다.
for _ in range(M):
    # product : 완제품이나 중간 부품, part : 중간 부품이나 기본 부품, amout : 필요한 양  
    product, part, amount = map(int, input().rstrip().split())
    
    # 완제품(중간 부품)을 위한 중간 부품(기본 부품)과 필요한 양을 저장한다.
    assembly_info[product].append([part, amount])

    # 사용된 중간 부품을 증가시킨다.
    part_info[part] += 1

# assembly_info를 출력해보면 아래와 같다.
# print(assembly_info)
# [[], [], [], [], [], [[1, 2], [2, 2]], [[5, 2], [3, 3], [4, 4]], [[5, 2], [6, 3], [4, 5]]]
# 1번부터 4번까지는 아무것도 없다. 즉, 기본 부품이라는 의미이다.

# part_info를 출력해보면 아래와 같다.
# print(part_info)
# [0, 1, 1, 1, 2, 2, 1, 0]
# 즉, 1~3번은 1개, 4~5번 제품은 2개, 6번 제품은 1개의 상위 제품(각 제품을 부품으로 하는 중간 or 완제품)이 존재한다는 의미이다.

# 부품들이 사용되는 개수를 표시할 리스트를 하나 만든다. 
amount_list = [0] * (N + 1)

# 사용된 부품을 표시하기 위한 리스트를 만든다.
visited = [0] * (N + 1)

# 기본 부품들을 넣어줄 리스트를 만든다.
essential_part = []

# 어느 제품의 상위 제품이 존재하지 않을 때까지
while sum(part_info) > 0:
    for part in range(1, N + 1):
        # 조합 정보가 존재하지 않고 사용하지 않았던 부품이라면
        if not assembly_info[part] and visited[part] == 0:
            # 기본 부품이다.
            essential_part.append(part)
            visited[part] = 1

        # 어떤 부품 N의 진입 차수가 0이고 사용하지 않았던 부품이라면, 
        if part_info[part] == 0 and visited[part] == 0:
            # 그리고 개수가 0이라면, 개수를 늘려주고 사용 표시를 해준다.
            if amount_list[part] == 0:
                amount_list[part] = 1
            visited[part] = 1
            # 해당 부품을 만드는 조합 정보들을 하나 씩 확인한다.
            for info in assembly_info[part]:
                # 각 부품 수량 리스트[하위 부품] += 하위 부품 필요 갯수 * 각 부품 수량 리스트[어떤 부품 N]
                amount_list[info[0]] += info[1] * amount_list[part]
                # part라는 부품을 만드는데 info[0]에 해당하는 부품을 한번 사용한 것이기 때문에 진입 차수를 감소시킨다. 
                part_info[info[0]] -=1

for part in essential_part:
    print(part, amount_list[part], sep=" ")
