

def solution(s:str)->str:
    a=set()

    for char in s:
        if char not in a:
            a.add(char)
    a=list(a)
    a=sorted(a)
    result=''
    for i in a:
        result+=i

    return result

if __name__ == '__main__':
    s="bcabc"
    print(solution(s))