from typing import List
import re
import collections
"""
    LeetCode 49
    
    1. How to Do:
        리스트 받아서 모두 sorting,  
    2. What I have learned:
        문자열 sorting 시에는 sorted(word)임 
        
        ## anagrams[''.join(sorted(word))] : dictionary 의 키값으로 설정해놓는 방법
        
        ''.join : 빈칸에 추가한다는 뜻이구나!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
    
"""
def anagram(wow:List[str])->List[List[str]]:

    anagrams=collections.defaultdict(list)  # default dictionary 인데 element가 list 인 녀석들
    for word in wow:
        anagrams[''.join(sorted(word))].append(word)    # append 하는이유는 리스트로 만들어서 계속 value 를 추가해줘야되기때문에!!!
    return anagrams
#    for word in wow:
#        anagrams[''.join(sorted(word))].append(word)
#    return anagrams.values()



def aanagram(wow:List[str])->List[List[str]]:

    anagrams=collections.defaultdict(list)
    for word in wow:
        anagrams[''.join(sorted(word))].append(word)

if __name__ == '__main__':
    #wow=[x for x in input("make the input please :").split()]
    wow=["eat","tea","tan","ate","ate","nat","bat"]
    print(anagram(wow))