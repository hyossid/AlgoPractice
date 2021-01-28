import collections


def solution(priorities, location):
    answer = 0
    # 인덱스와 우선순위가 같이 담긴 리스트
    maxpri = 0
    numbers = []
    for i, p in enumerate(priorities):
        numbers.append([i, p])
        maxpri = max(maxpri, p)
    s=0
    sequence = []
    # numbers 를 큐처럼
    while numbers:
        cur = numbers.pop(0)
        if maxpri == cur[1]:
            s=0
            sequence.append(cur)
            for v in numbers:
                s=max(s,v[1])
                maxpri=s
            # 각 priority 개수들 처리해줘야한다
        else:
            numbers.append(cur)

    for i in range(len(sequence)):
        if sequence[i][0] == location:
            answer = i

    return answer+1



def solution2(priorities,location):
    answer=0
    from collections import deque
    d=deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item=d.popleft()
        if d and max(d)[0]>item[0]:
            d.append(item)
        else:
            answer+=1
            if item[1]==location:
                break
    return answer

if __name__ == '__main__':
    print(solution([2,1,3,2],2))