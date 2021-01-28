import copy
from typing import List

"""
    From 1 to N, we have to return the possible combination of 2
"""

def combine(n: int, k: int) -> List[List[int]]:
    results=[]

    def dfs(elements,start,k):
        if k==0:
            results.append(elements[:])
            return
        else:
            for i in range(start,n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)   # 최소 한번 append 하고 여기서 튀어나오니까, pop()이 이제서야 이해가 되는거 같다.
                elements.pop()
    dfs([],1,k)
    return results


def combine2(lists,k) -> List[int]:
    results=[]
    def dfs(elements,start,k):
        if k==0:
            results.append(elements[:])
            return
        else:
            for i in range(start,len(lists)):
                elements.append(lists[i])
                dfs(elements,i+1,k-1)   ####아악!!!!!!!!!!
                elements.pop()

    dfs([],0,k)
    return results


def solution(list,k):
    results=[]
    def dfs(elements,start,k):
        if k==0:
            results.append(elements[:])
            return
        else:
            for i in range(start,len(list)):
                elements.append(list[i])
                dfs(elements,i+1,k-1)
                elements.pop()


    dfs([],0,k)



if __name__ == '__main__':
    #print(combine(5,3))
    print(combine2([2,3,4,5,6],3))