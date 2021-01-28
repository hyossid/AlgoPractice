from typing import List
import collections
def minSubArrayLen(s: int, nums: List[int]) -> int:
    maxs = len(nums);  # Max value to be saved
    left=0
    sums=0
    for i in range(len(nums)):
        sums+=nums[i]
        while(sums>=s):
            maxs=min(maxs,i+1-left)
            sums-=nums[left]
            left+=1
    return maxs

    # while winsize<=len(nums):
    #     end=start+winsize
    #     while end<len(nums):
    #         if s<=sum(nums[start:end+1]):
    #             return winsize+1
    #         start+=1
    #         end+=1
    #     winsize+=1
    #     start=0
    return 0


if __name__ == '__main__':
    print(minSubArrayLen(7,[2,3,1,2,4,3]))