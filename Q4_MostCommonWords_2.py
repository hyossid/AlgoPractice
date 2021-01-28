from typing import List
import re
import collections

"""
    1. What to do:
        lowercase로 통일 : regular expression
        ## 참 좋은 코딩 :
        ## k=[i for i in re.sub(r'[^\w]',' ',para).lower().split() if i not in banned] 
    
"""
def CommonWords(para:str,banned:List[str])->str:
    k=[i for i in re.sub(r'[^\w]',' ',para).lower().split() if i not in banned]
    n=collections.Counter(k)
    m=n.most_common(1)
    return m[0][0]




if __name__ == '__main__':
    para="Bob hit a ball, the hit BALL flew far after it was hit."
    banned=["hit"]
    print(CommonWords(para,banned))