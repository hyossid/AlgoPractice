from typing import List
import re
import collections

"""
    LeetCode #937

    1. What to do : 
        identifier 대로 분리, 두개의 리스트를 사용
    2. What I've learned
        split 은 String에서만 쓸수있으면 기본값은 띄어쓰기로 나누는것이다.
        range 쓰면 int가되는걸 잊지말자!!!
        
        sort 시에, key= 로 정렬 기준을 변경할 수 있다. (정해진 변수임, len,,,fn(함수 리턴값))
        Lambda 
"""
def solution(logs:List[str])->List[str]:
    letters,digits=[],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
    return letters+digits

def logfunction(logs:List[str])->List[str]:
    digit=[]
    letter=[]
    for log in logs:
        if 'digi' in log.split()[0]:
            digit.append(log)
        else:
            letter.append(log)
    return letter + digit



if __name__ == '__main__':
    logs=["digi1 8 1 5 1","let1 art can","digi2 3 6","let2 own kt dig","let3 art zero"]
    print(logfunction(logs))
