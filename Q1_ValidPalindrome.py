from typing import List
import re
import collections
"""
    Leetcode #125
    What to do: 
    1. Preprocess to a string with only lower case
    
    What I have learned from this problem : 
    
        1. 리스트를 pop(0), pop() 해서 앞뒤를 동일한지 비교하는것
        2. [::-1]을 쓰는법
        3. 정규식 사용해서 문자열 건들이는법 
"""


if __name__ == '__main__':
    s="A man, a plan, a canal : Panama"
    s=s.lower()
    n=[c for c in re.sub('[^a-z0-9]','',s)]

    while len(n)>0:
        if n.pop(0)!=n.pop():
            print(False)

    #if n[::-1]==n:
    #    print(True)
