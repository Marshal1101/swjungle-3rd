# 김재현

import math
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

class  Solution:
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
    
    def get_GB_partition(self, num):
        for i in range(int(num/2), 0, -1):
            if self.check_prime_num(i):
                if self.check_prime_num(num - i):
                    return [i, num - i]


if __name__=="__main__":
    sol = Solution()
    result = []
    for i in data:
        result.append(sol.get_GB_partition(i))
    for pair in result:
        print(str(pair[0]) + " " + str(pair[1]))
