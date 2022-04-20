from nis import match
import re

# logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

# 수집하지 않는 로그의 갯수!
# 100자 이하

answer = 0
startEndProblem = re.compile("^[a-zA-Z](.)*[a-zA-Z]$")
multipleSpacingProblem = re.compile("(.)*\s\s(.)*")
notAlphabet = re.compile("[^a-zA-Z]")
for log in logs:
    if not startEndProblem.match(log) or multipleSpacingProblem.match(log):
        answer += 1
        continue
    if len(log) > 100:
        answer += 1
        continue
    logElem = list(log.split(" "))
    if len(logElem) != 12:
        answer += 1
        continue
    if logElem[0] != "team_name" or logElem[3] != "application_name" or logElem[6] != "error_level" or logElem[9] != "message" or not (logElem[1] == logElem[4] == logElem[7] == logElem[10] == ":"):
        answer += 1
        continue
    if notAlphabet.match(logElem[2]) or notAlphabet.match(logElem[5]) or notAlphabet.match(logElem[8]) or notAlphabet.match(logElem[11]):
        answer += 1
        continue

print(answer)