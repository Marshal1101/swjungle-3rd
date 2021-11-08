import sys
import math

n = int(input())
data = list(map(int,sys.stdin.readline().split()))


def checker(n, data):
    count = 0
    for num in data:
        if num == 1:
            continue
        elif num == 2 or num == 3 or num == 5 or num == 7:
            count +=1
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            continue
        else:
            sqrt_i = int(math.sqrt(num))
            j = 1
            PMchecker = True
            for j in range(2, sqrt_i + 1):
                if num % j == 0:
                    PMchecker = False
                    break
            if PMchecker == False:
                continue
            else:
                count += 1
    return count

print(checker(n, data))

# 1978