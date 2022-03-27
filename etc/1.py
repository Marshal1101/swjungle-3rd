logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

def solution(logs) :
    def checkAlphabet(input) :
        # print('checkA', type(input))
        if input.isupper() or input.islower() :
            length = 0
            for i in input:
                length += 1
            # print('input_length', length)
            return length
        return 0

    def checkLength(input) :
        length = 0
        space = 0
        for i in input:
            length += 1
            if i == ' ' :
                space += 1
        return [length, space]

    count = 0
    for taem in logs :
        print(taem)
        length = 0
        log = taem.split(' : ')
        # print(checkLength(log[0]))
        if log[0].lstrip() != 'team_name' :
            count += 1
            print('0 error', count)
            continue
        length += checkLength(log[0])[0]
        application_name = log[1].split(' ')
        len = checkAlphabet(application_name[0])
        if len == 0 or application_name[1] != 'application_name' :
            count += 1
            print('1 error', count)
            continue
        length += len + 16
        error_level = log[2].split(' ')
        len = checkAlphabet(error_level[0])
        if len == 0 or error_level[1] != 'error_level' :
            count += 1
            print('2 error', count)
            continue
        length += len + 11
        message = log[3].split(' ')
        len = checkAlphabet(message[0])
        if len == 0 or message[1] != 'message' :
            count += 1
            print('3 error', count)
            continue
        length += len + 7
        # print('log[4]', log[4])
        len = checkAlphabet(log[4].rstrip())
        if len == 0 :
            count += 1
            print('4 error', count)
            continue
        length += checkLength(log[4])[0]
        if length > 100 :
            count += 1
            print('100 over error', count)
        print('length', length)

    return count

print(solution(logs))