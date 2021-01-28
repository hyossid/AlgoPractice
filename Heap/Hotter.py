def mix(lst):
    lst.sort()
    score=lst[0]+2*lst[1]
    lst.pop(0)
    lst[0]=score
    return lst
def solution(scoville, K):
    answer=0
    scoville.sort()
    while scoville[0]<K:
        if len(scoville)>=2:
            scoville=mix(scoville)
            answer+=1
        else:
            return -1
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12],7))