from typing import List
import re
import collections
"""
    What Ive learned : 
        항상 인덱스가 필요할때는 enumerate 를 떠올리자.
        
    짚고 넘어가야할 부분 : 다 브루트포스로 돌리지말고, 타겟 - n 으로 돌리면 더 아낄수 있음. 
        그리고 딕셔너리를 잘 사용하면 o(n2)을 o(n)으로 바꿔버릴수도있다!!!!!
        
"""
def twosumdefault(nums:List[int])->List[str]:

    result=[]
    for i in range(len(nums)):
        for j in range (i,len(nums)):
            if nums[i]+nums[j]==target:
             result.append([i,j])
    return result

def twosumtwopoint(nums:List[int])->str:
    d=collections.defaultdict(list)
    for i,v in enumerate(nums):
        d[v]=i

    for i,v in enumerate(nums):
        if target-v in d and i!=d[target-v]:
            return nums.index(v),d[target-v]


if __name__ == '__main__':
    nums=[2,7,11,15]
    target=9

    print(twosumtwopoint(nums))