from operator import length_hint


sentences = ["ABcD", "bdbc", "a", "Line neWs"]
n = 7

def solution(sentences, n) :

    def check_point_usedKey(input) :
        length = 0
        upper = 0
        used_key = set()
        for i in input:
            length += 1
            used_key.add(i)
            if i.isupper() :
                upper += 1
                used_key.add('shift')
        total_point = length + upper

        used_key.discard(' ')
        
        return [total_point, used_key]
        

    N = len(sentences)
    max_point = 0
    sorted_list = []     
    for i in range(N) :
        sorted_list.append(check_point_usedKey(sentences[i]))
    sorted_list.sort(reverse=True)

    tot = 0
    for i in range(N) :
        point = sorted_list[i][0]
        charset = sorted_list[i][1]
        for j in range(i+1, N) :
            # print(sorted_list[j][1])
            new_set = charset.union(sorted_list[j][1])
            # print(new_set)
            length = len(new_set)
            if length <= n :
                charset = new_set
                point += sorted_list[j][0]
        if point > tot :
            tot = point

    print(sorted_list, tot)

solution(sentences, n)