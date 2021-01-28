from typing import List
import re
import collections


def ThreeSums(nums:List[int])->List[List[int]]:
    nums.sort()
    results=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-2]:
            continue





if __name__ == '__main__':
    nums=[-1,0,1,2,-1,-4]
    print(ThreeSums(nums))