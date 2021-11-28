## 02 1904 01타일 (참조, https://uneducatedjungler.tistory.com/100?category=970202)
## 피보나치 수열

n = int(input())
list = [0, 1, 0]
for i in range(n) : 
    list[2] = (list[0] + list[1]) % 15746
    list[0], list[1] = list[1], list[2]
print(list[min(n, 2)])