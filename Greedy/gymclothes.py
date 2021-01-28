def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    plost=lost[:]
    # remove 가 lost 인덱스에 영향을 미치니까 이렇게 하면 안된다.
    for v in lost:
        if v in reserve:
            reserve.remove(v)
            plost.remove(v)
    lost=plost[:]
    for v in lost:
        if v - 1 in reserve:
            reserve.remove(v - 1)
            plost.remove(v)
            continue
        if v in reserve:
            reserve.remove(v)
            plost.remove(v)
            continue
        if v + 1 in reserve:
            reserve.remove(v + 1)
            plost.remove(v)
            continue

    return n - len(plost)

if __name__ == '__main__':
    print(solution(	3, [1, 2], [2, 3]))