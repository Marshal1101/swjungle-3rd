# 김재현

#소수의 개수 출력
#에라토스테네스의 체
import math
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

class Solution:
    def check_prime_num(self, num):
        if num < 2 :
            return 0
        top = int(math.sqrt(num)) + 1
        divsor_flag = 1
        for i in range(2, top):
            if num % i == 0 :
                divsor_flag = 0
                break ;
        return divsor_flag

if __name__ == "__main__":
    sol = Solution()
    count = 0
    for item in data:
        if (sol.check_prime_num(item)):
            count += 1
    print(count)