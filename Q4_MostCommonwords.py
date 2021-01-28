from typing import List
import re
import collections

def CommonWord(para:str,banned:List[str])->str:

    words=[word for word in re.sub(r'[^\w]',' ',para).lower().split() if word not in banned]
    counts=collections.Counter(words)   # 리스트에서 나타나는 개수대로
    return counts.most_common(1)[0][0]


def CommonWords(para:str,banned:List[str])->str:
    words=[word for word in re.sub(r'[^\w]',' ',para).lower().split() if word not in banned]
    counts=collections.Counter(words)
    ans=counts.most_common(1)[0][0]

    return ans



if __name__ == '__main__':
    para="Bob hit a ball, the hit BALL flew far after it was hit."
    banned=["hit"]
    print(CommonWords(para,banned))
