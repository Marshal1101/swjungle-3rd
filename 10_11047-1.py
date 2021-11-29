## 10 11047 동전 0 (참조, 백준 빠른 문제 풀이)


N, K = map(int, input().split())

Coins = []
for i in range(N) : Coins.append(int(input()))


ans = 0
while K > 0 :
    coin = Coins.pop()
    ans += K // coin
    K %= coin

print(ans)