## 01 2748 피보나치 수 2 (구현 : 01)


import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (100)
dp[1] = 1
dp[2] = 1

def Fibonacci(n) :
    if n == 1 or n == 2:
        return 1
    if dp[n] != 0 :
        return dp[n]
    else :
        dp[n] = Fibonacci(n-1) + Fibonacci(n-2)
        return dp[n]
    
print(Fibonacci(n))