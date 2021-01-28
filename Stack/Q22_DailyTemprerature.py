
from typing import List

def solution(T:List[int]):
    answer=[0]*len(T)
    stack=[]
    cur=0
    for i,cur in enumerate(T):
        while stack and cur>T[stack[-1]]:
            last=stack.pop()
            answer[last]=i-last
        stack.append(i)
    return answer


def solutionn(T):
    ans=[0]*len(T)
    stack=[]

    for i,cur in enumerate(T):
        while stack and T[stack[-1]]<cur:
            last=stack.pop()
            ans[i]=last-i
        stack.append(i)

    # 두번째 부터 돌게 하는 방법

    for i,cur in enumerate(T):

        while stack and T[stack[i]]<cur:
            last=stack.pop()
            ans[last]=last=i
        stack.append(i)


if __name__ == '__main__':
    T=[73,74,75,71,69,72,76,73]