from typing import List


def solution(numbers:List[int],target:int)->int:

    length=len(numbers)
    global cnt
    cnt=0
    def dfs(i,sum):
        if i==length:
            if sum==target:
                global cnt
                cnt+=1
            return
        dfs(i+1,sum+numbers[i])
        dfs(i+1,sum-numbers[i])

    dfs(0,0)
    a=cnt
    return a


if __name__ == '__main__':
    numbers=[1,1,1,1,1]
    target=3
    print(solution(numbers,target))