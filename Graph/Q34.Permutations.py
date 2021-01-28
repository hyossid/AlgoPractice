
from typing import List

def solution(nums):

    results=[]
    prevelements=[]

    def dfs(elements):

        if(len(elements))==0:
            results.append(prevelements[:])

        for e in elements:
            nextelements=elements[:]
            nextelements.remove(e)

            prevelements.append(e)
            dfs(nextelements)
            prevelements.pop()

    dfs(nums)
    return results


def solution2(lst):
    results=[]
    prvelements=[]
    def dfs(elements):
        if len(elements)==0:
            results.append(prvelements[:])
            return
        else:
            for v in elements:
                nextelements=elements[:]
                nextelements.remove(v)
                prvelements.append(v)
                dfs(nextelements[:])
                prvelements.pop()
    dfs(lst)
    return results





if __name__ == '__main__':
    nums=[1,2,3]
    print(solution(nums))