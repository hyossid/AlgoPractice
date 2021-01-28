
from typing import List

def mergesort(nums:List[int])->List[int]:

    if len(nums)==1:
        return
    n=len(nums)
    b=n/2
    lst1=nums[:b]
    lst2=nums[b:]
    mergesort(lst1)
    mergesort(lst2)

def merge(left,right):
    v=list()
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            v.append(left[i])
            i+=1
        else:
            v.append(right[j])
            j+=1
        if i==len(left) :
            v=v+right[j:len(right)]
        if j==len(right):
            v=v+left[i:len(left)]

        return v
def merge_sort(v):
    if len(v)<=1:
        return v
    m=len(v)//2
    left=merge_sort(v[:m])
    right=merge_sort(v[m:])
    return merge(left,right)

if __name__ == '__main__':
    nums=[12,43,241,2355,43523,123,5432,1345,6554,243]
    print(mergesort(nums))