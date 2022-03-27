from numpy import array


arr = [3, 7, 2, 4]
brr = [4, 5, 5, 2]


def solution(arr, brr) :
    i = 0
    count = 0
    while True :
        try :
            gab = arr[i] - brr[i]
            # print('gab', gab)
            if gab == 0 :
                try :
                    i += 1
                    continue
                except :
                    return count
            else :
                arr[i] -= gab
                arr[i+1] += gab
            count += 1
            i += 1
        except :
            return count

print(solution(arr, brr))