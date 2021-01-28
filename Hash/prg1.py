import collections


def solution(n, lost, reserve):
    answer = n - len(lost)

    for v in lost:
        if v in reserve:
            reserve.remove(v)
            lost.remove(v)
            answer += 1

    for v in lost:
        if v + 1 in reserve:
            reserve.remove(v + 1)
            answer += 1
            continue
        elif v - 1 in reserve:
            reserve.remove(v - 1)
            answer += 1
            continue
        else:
            continue
    return answer
if __name__ == '__main__':
    print(solution(4,[1,2,3,4],[1,2,3,4]))