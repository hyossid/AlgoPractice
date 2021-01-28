from typing import List
ans=[]
def permute(nums: List[int]):

    def recurse(lst,cops):
        if len(lst)==len(nums):
            ans.append(lst)
            return
        else:
            for v in cops:
                lst.append(v)
                cops.remove(v)
                recurse(lst,cops)
    lss=[]
    cops=nums[:]
    recurse(lss,cops)

    return ans

if __name__ == '__main__':
    nums=[1,2,3]
    print(permute(nums))
