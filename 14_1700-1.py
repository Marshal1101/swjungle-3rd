## 14 1700 멀티탭 스케줄링(참조, https://pacific-ocean.tistory.com/357)

from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
s = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0
for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            try:
                if a < s[i + 1:].index(m[j]):
                    a = s[i + 1:].index(m[j])
                    b = j
            except:
                a = -1
                b = j
                break
        m[b] = s[i]
        cnt += 1
print(cnt)


# 우선 멀티탭이 비어있는지, 혹은 꽂으려고 하는 플러그가 있는지 확인을 한다.
# 둘중 하나가 True라면 해당 플러그를 꽂고 continue해준다.
# 그게 아니라면 플러그 하나를 뽑아야 한다.
# 다시 사용되지 않는 플러그를 우선적으로 뽑아주고
# 꽂혀있는 플러그중에서 가장 나중에 사용되는 플러그를 뽑아준다.