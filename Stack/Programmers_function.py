import math


def solution(progresses, speeds):
    answer = []
    days = []
    for a, b in zip(progresses, speeds):
        days.append(math.ceil((100 - a) / b))
    while len(days)!=0:
        cnt=1
        a=days.pop(0)
        dayss=days[:]
        for i in range(len(days)):
            if a>days[i]:
                cnt+=1
                dayss.pop(0)
            else:
                break
        answer.append(cnt)
        days=dayss[:]
    return answer

if __name__ == '__main__':
    print(solution([99,96,98,97],[1,1,1,1]))