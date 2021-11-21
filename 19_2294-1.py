## 19 2294 동전2 (참조)
# BFS


import sys
from collections import deque

# 전체 동전의 수와 목표 금액을 입력 받는다.
coin_num, target_won = map(int, sys.stdin.readline().split())

# 동전 종류를 입력 받는다.
# 세트를 사용하는 이유는 가치가 같은 동전이 여러 번 주어질 수 있기 때문이다.
coin_set = set(int(sys.stdin.readline()) for _ in range(coin_num))
# print(coin_set)

# 동전 사용 여부를 표시해준다.
check_coin = [0 for _ in range(target_won + 1)]
# print(check_coin)

queue = deque()
# 동전 세트에서 동전을 하나씩 꺼낸다.
for coin in coin_set:
    # 꺼낸 동전이 목표 금액보다 크면 패스
    if coin > target_won :
        continue
    # 아니라면, 해당 동전을 queue에 넣어준다.
    queue.append([coin, 1])
    # 그리고 해당 동전 사용 여부를 표시해준다.
    check_coin[coin] = 1

result = -1
while queue:
    # queue에서 현재 동전 금액과 해당 금액을 만들기 위해 사용한 동전 개수를 뽑는다.
    current_coin, count = queue.popleft()
    # 현재 동전 금액이 목표 금액과 같다면
    if current_coin == target_won:
        # 사용한 동전 개수를 출력한다.
        print(count)
        result = 0
        break
    # 동전 세트에서 동전을 하나 씩 다시 꺼낸다.
    for coin in coin_set:
        # 현재 동전 금액에 꺼낸 동전을 더한 금액이 목표 금액보다 크면 패스
        if current_coin + coin > target_won:
            continue
        # 현재 동전 금액에 꺼낸 동전을 더한 금액이 처음 나온 조합이라면
        if check_coin[current_coin+coin] == 0:
            # 사용 여부를 표시해주고
            check_coin[current_coin+coin] = 1
            # target_won을 만들 수 있는 후보 조합으로서 queue에 넣어준다.
            queue.append([current_coin+coin, count + 1])

if result:
    print(result)