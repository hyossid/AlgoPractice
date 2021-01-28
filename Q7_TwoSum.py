from typing import List
import re
import collections


def twosum(nums:List[int],target):
    for i in range(len(nums)):
        for j in range(len(nums)-i):
            if nums[i]+nums[j]==target:
                return i,j



if __name__ == '__main__':
    nums=[2,7,11,15]
    target=9
    print(twosum(nums,target))