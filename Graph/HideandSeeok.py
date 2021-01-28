


import collections
# 얼마나 빨리 a가 b에 도착할지.

def solution(a,b)->int:
    Q=collections.deque()
    Q.append((a,0))
    check=list()

    while len(Q)!=0:
        cur,cnt=Q.popleft()
        if cur+1==b or cur-1==b or 2*cur==b:
            break
        else:
            Q.append((cur+1,cnt+1))
            Q.append((cur-1,cnt+1))
            Q.append((2*cur,cnt+1))

    return cnt+1


if __name__ == '__main__':
    a, b = map(int, input().split())
    answer=solution(a,b)
    print(answer)