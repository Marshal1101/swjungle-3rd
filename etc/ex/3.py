num_teams, remote_tasks, office_tasks, employees = 3, ["development","marketing","hometask"], ["recruitment","education","officetask"], ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

answer = set()

teamOffice = [0]*(num_teams+1)
for i in range(len(employees)):
    haveOfficeTask = 0
    eElem = list(employees[i].split(" "))
    for j in range(1, len(eElem)):
        if eElem[j] in office_tasks:
            haveOfficeTask += 1
    if not haveOfficeTask:
        answer.add(i+1)
    else:
        teamOffice[int(eElem[0])] += 1

teamHead = [0]*(num_teams+1)
for i in range(len(employees)):
    emplyee = employees[i]
    if teamHead[int(emplyee[0])] == 0:
        teamHead[int(emplyee[0])] = i+1

for i in range(1, num_teams+1):
    if teamOffice[i] == 0:
        print(teamHead[i])
        answer -= {teamHead[i]}

print(list(answer))