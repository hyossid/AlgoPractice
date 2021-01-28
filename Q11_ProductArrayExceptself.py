from typing import List



def prodself(n:List[int])->List[int]:
    a=[]
    prod=1
    for i in range(len(n)):
        for j in range(len(n)):
            if i==j:
                continue
            prod*=n[j]
        a.append(prod)
        prod=1
    return a

def proddself(n:List[int])->List[int]:
    a=[]
    prod=1
    for i in range(len(n)):
        
if __name__ == '__main__':
    n=[1,2,3,4]
    print(prodself(n))