from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    results = []

    def dfs(arr, index):
        if arr not in results:
            results.append(arr[:])

        for i in range(index, len(nums)):
            temp = arr[:]
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            dfs(temp, index + 1)
            temp.pop()

    dfs([], 0)
    return results

if __name__ == '__main__':
    print(subsets([1,2,3]))