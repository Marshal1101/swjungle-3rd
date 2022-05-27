## 81 11054 가장 긴 바이토닉 부분 수열
# (참조, https://pacific-ocean.tistory.com/158)


import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
dpp = [0 for i in range(n)]
dpm = [0 for i in range(n)]
dpb = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1
for i in range(n):
    dpb[i] = dpp[i] + dpm[i] - 1
print(max(dpb))


# 위의 문제를 정방향으로 for문을 돌려주고, 역방향으로도 for문을 돌려
# 둘이 합치면 바이토닉 부분 수열이 나온다.
# 바이토닉 부분 수열중 가장 큰 값을 출력해준다.