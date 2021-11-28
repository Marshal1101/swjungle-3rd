## 03 9084 동전 (참조, dkkim012)


import sys
input = sys.stdin.readline

def find_num(coin_list, target_number):
    dp = [0]*(target_number+1)
    
    for coin in coin_list:
        if coin > target_number:
            continue
        dp[coin] += 1  # 자기 자신 추가
        for i in range(coin, target_number+1): # 자기 자신보다 큰 것만 보면 된다.
            dp[i] = dp[i] + dp[i-coin] # 가장 작은 coin부터 쌓아올린 경우의 수 + 내가 더해짐으로서 얻을 수 있는 경우의 수
    
    return dp[target_number]

if __name__=='__main__':
    test_num = int(input().strip())

    for i in range(test_num):
        coin_num = int(input().strip())
        coins = list(map(int, input().split()))
        target = int(input().strip())

        print(find_num(coins, target))