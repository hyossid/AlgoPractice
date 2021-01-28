

def ladder(n:int):

    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        cache=[0]*n
        cache[1]=1
        cache[2]=2
        for i in range(3,n+1):
            cache[i]=cache[i-1]+cache[i-3]
        return cache[n]





if __name__ == '__main__':
    print(ladder(9))