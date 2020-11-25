#문제 https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
#문제 알고리즘 : 시뮬래이션


def solution(record):
    answer = []
    real_answer = []
    user_dic = dict()
    for i in record:
        temp = i.split()
        if temp[0]=='Enter':
            user_dic[temp[1]] = temp[2]
            answer.append(f"{temp[1]}#님이 들어왔습니다.")
        if temp[0]=='Leave':  
            answer.append(f"{temp[1]}#님이 나갔습니다.")
        if temp[0]=='Change':
            user_dic[temp[1]] = temp[2]   
    for i in answer:
        temp = i.split('#')
        real_answer.append(user_dic.get(temp[0])+temp[1])
        temp = []
    return real_answer
