sentences, n = ["line in line", "LINE", "in lion"], 5
tmp = {}
for sentence in sentences:
    for i in range(len(sentence)):
        if tmp.get(sentence[i]):
            tmp[sentence[i]].append(i)
        else:
            tmp[sentence[i]] = [i]
    print(tmp)