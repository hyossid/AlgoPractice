


def compare(a,b):
    c=eval(str(a)+str(b))
    d=eval(str(b)+str(a))
    if a<b:
        return 1
    else:
        return 0

def solution(inlist):

    i=1
    while i<len(inlist):
        j=i
        while j>0 and compare(inlist[j-1],inlist[j]):
            inlist[j-1],inlist[j]=inlist[j],inlist[j-1]
            j-=1
        i+=1
    return str(int(''.join(map(str,inlist))))



if __name__ == '__main__':
    print(solution([3,30,34,5,9]))