def changer(list):
    length = len(list)
    if length <= 1:
        return list
    for i in range(1, length):
        if list[0] < list[i]:
            return changer(list[1:i]) + changer(list[i:]) + [list[0]]
    return changer(list[1:]) + [list[0]]


list = [50, 30, 24, 5, 28, 45, 98, 52, 60]

changer(list)