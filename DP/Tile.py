


d=[0]*1001
def solution(num):
    if num==0:
        return 1
    if num==1:
        return 2
    if num==2:
        return 7
    if d[num]!=0:
        return d[num]
    result=2*solution(num-1) + 3*solution(num-2)
    for i in range(3,num+1):
        result+=2*solution(num-i)                       ## 이 경우도 dp를 한번 더 사용해 볼 수 있지 않을
    d[num]=result
    return result




if __name__ == '__main__':
    print(solution(3))
