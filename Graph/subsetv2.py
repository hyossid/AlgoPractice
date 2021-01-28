from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    results = []

    def dfs(path,index):
        results.append(path)

        for i in range(index,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            dfs(path+[nums[i]],i+1)

    dfs([], 0)

    return results

if __name__ == '__main__':
    print(subsetsWithDup([1,2,2]))