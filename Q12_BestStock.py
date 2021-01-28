from typing import List

"""
    LeetCode # 121
    
    What to do :
        1. iterate -> max() 사용해서 최대의 차이값을 알아내야함
        2. 
    What Ive learned :
    
        외우자이거, 
        for문 돌때, 그 시점에서의 제일 큰 차를 구할 수 있음.   
        sys.maximize 라는걸 쓰는것    
"""

def stock(n:List[int])->int:
    maxi=0
    for i,v in enumerate(n):
        for j in range(i,len(n)):
            maxi=max(maxi,n[j]-v)

    return maxi

def effectivestock(n:List[int])->int:
    result=0
    flag = False
    minval=n[0]
    minvalindex=0
    for i,a in enumerate(n):
        if minval>a:
            minval=a
            minvalindex=i
    # now minval and minvalindex is set

    for i,num in enumerate(n):
        if minvalindex<i:
            if num>minval:
                result=max(result,num-minval)

    return result



def maxProfit(self, prices: List[int]) -> int:
    profit=0
    minprofit=sys.maxsize

    for price in prices:
        minprofit=min(minprofit,price)
        profit=max(profit,price-minprofit)

    return profit




def solution(n):

    for i,v in enumerate(n):
        mini=min(mini,v)
        ans=max(ans,v-mini)
    return ans




if __name__ == '__main__':
    n=[7,1,5,3,6,4]
    print(effectivestock(n))