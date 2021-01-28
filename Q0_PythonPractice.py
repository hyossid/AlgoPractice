from typing import List
import re
import collections

"""
1. Generator
    - Range : 주로 for 문이랑 같이쓴다. range(2,100) 으로 첫값을 정해줄수 있다. ""하지만 마지막-1 까지만 접근한다.""
    - Enumerate : 인덱스랑 같이 리턴한다. List, Dictionary 까지 Iterate 가능하며, Dictionary enumerate 시에는 Key 랑 대응함
2. List Comprehension
    - 리스트를 기반으로 새로운 리스트를 만들어낸다. 형식을 기억하자.
      ##  n = range (1,101) #     1부터 100까지
      ##  a=[i*2 for i in n if i%2==0 ]
      ##  n= [i for i in range(1,101)] # 100 까지 리스트 쉽게 뽑기

3. List Splitting
    - n[1:3] 일때 n[1],n[2] 를으로 리턴해준다. 인덱스 기준이며, 마지막은 제외된다는 것을 잊지말자!!
    - n.count(k) : n에서 k 의 개수 , n.index(k) : n에서 k의 인덱스 
    - n[:-3] 뒤에서 3번째까지 리스트로 만들어준다.
    - n[-3:] 뒤에서 3번째부터 끝까지
    - n[::-1] 뒤집기
    - n[::2] 첫번째 원소부터 두칸씩 건너뛰어서 저장한다. 
    
4. Dictionary
    - for k,v in d.items() : 각각의 key 와 value 꺼내온다  
    - collections.defaultdict(int) : 딕셔너리를 생성하되, 기본값이 0, keyError가 안뜨도록
    - collections.Counter(리스트) : 아이템의 개수를 딕셔너리로 만들어준다!!!!!!!!!!!!!
##- k 가 collection.coutner 일때, k.most_common(2) 하면 가장흔한거 2개 리스트안에 튜플있는 형태로 돌려줌
"""


if __name__ == '__main__':

    l=[1,2,3,4,5,55,5,5,5,5,5,6,7,8,7,8,8,8,8]
    k=collections.Counter(l)

    print(type(k.most_common(2)[0]))