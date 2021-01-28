
from typing import List

"""
    23을 받았다고 치자
"""
def practice(s:str):
    dic = {'2': "abc", '3': "def", '4': 'ghi', '5': 'jkl', '6': "mno", '7': 'pqr', '8': 'stu', '9': 'wxyz','0': '+'}
    result=[]
    def func(index,path):
        # BackTracking
        if len(path)>len(s):
            return

        for j in dic[s[index]]:
            result.append(path)
            func(index+1,path+j)
    func(0,"")
    return result











def solution(num:int)->List[str]:
    dic={'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':"mno",'7':'pqr','8':'stu','9':'wxyz','0':'+'}

    r=str(num)
    ls=list()
    for ch in r:
        #print(type(dic['ch']))
        ls.append(list(dic[ch]))        # ch 이거 'ch' 로 넣으면 안된다....

#    ls[0]


def realsolution():
    digits="234"
    def dfs(index,path):
        if len(path)==len(digits):
            result.append(path)
            return
        for i in range(index,len(digits)):
            for j in dic[digits[i]]:
                dfs(index+1,path+j)
    if not digits:
        return []

    dic = {'2': "abc", '3': "def", '4': 'ghi', '5': 'jkl', '6': "mno", '7': 'pqr', '8': 'stu', '9': 'wxyz','0': '+'}
    result=[]
    dfs(0,"")
    return result


def practice2(s:str):

    def dfs(index,path):
        if(len(path)==len(s)):
            result.append(path)
            return
        for i in range(index,len(s)):   #234
            for j in dic[s[i]]:
                dfs(index+1,path+j)

    dic = {'2': "abc", '3': "def", '4': 'ghi', '5': 'jkl', '6': "mno", '7': 'pqr', '8': 'stu', '9': 'wxyz','0': '+'}

    result=[]
if __name__ == '__main__':
    #num=input()
    print(realsolution())