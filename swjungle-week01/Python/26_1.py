# 하노이 탑 
# 1914

import sys

n = int(sys.stdin.readline())
a = 1
b = 3
printbreak = True if n > 20 else False
print(2**n - 1)
def hanoii(n, x, y):
    ## n = 개수, a = 시작지점, b = 목표지점
    if n > 1:
        hanoii(n - 1, x, 6 - x - y)

    if printbreak != True:
        print(x, y)
    
    if n > 1:
        hanoii(n - 1, 6 - x - y, y)

if n<=20:
    hanoii(n, a, b)

## 시간초과