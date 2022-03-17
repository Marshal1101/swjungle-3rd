# 9020
import sys
import math

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
def Prime_checker1(num):
    if num < 2:
        return 0
    else:
        sqrt_i = int(math.sqrt(num))
        for j in range(2, sqrt_i + 1):
            if num % j == 0:
                return 0
                # break
        return 1

# def Prime_checker2(num);
# def goldbach_partition(list):
for i in data:
    # if i % 2 :
    #     break
    # else:
    half_num = int(i / 2)
    d = 2
    up_num = half_num + 1
    down_num = i - up_num 
    if Prime_checker1(half_num) == 1:
        print(f'{half_num} {half_num}')
    else:
        while True:
            if Prime_checker1(up_num) == 1:
                break
            up_num += d
            down_num = i - up_num
        print(f'{down_num} {up_num}')

# goldbach_partition(data)


## 시간초과