def ntimes():
    n = int(input())
    i = 1
    while i < 10:  # 1~9
        print(n, '*', i, '=', n*i)
        i += 1

if __name__ == '__main__':
    ntimes()