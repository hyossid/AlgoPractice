from typing import List
import re
import collections
"""
 LeetCode #5 
 
 max 도 key=len 할수있다.
"""
def ssss():

    def expand(left:int,right:int)->str:
        while left>=0 and right <=len(s) and s[left]==s[right-1]:
            left-=1
            right+=1
        return s[left+1:right-1]

    # 바로 끝나버리는 경우
    if len(s)<2 or s==s[::-1]:
        return s

    result = ''

    for i in range(len(s)-1):
        result = max(result,expand(i,i+1),expand(i,i+2),key=len)



def solution(str):
    def expand(left,right):
        while left>=0 and right<=len(str) and str[left]==str[right-1]:
            left-=1
            right+=1
        return str[left+1:right-1]
    if len(str)<2 or str==str[::-1]:
        return str
    result=""
    for i in range(len(str)-1):
        result=max(result,expand(i,i+1),expand(i,i+2),key=len)
    return result
if __name__ == '__main__':
    s="babad"
    print(solution(s))







