
fib=[]

def fibonacci(num)->int:
    if num==1 or num==2:
        fib[num]=num
        return 1
    elif num==0:
        fib[num]=num
        return 0
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def dp_fib(num)->int:
    cache=[0]*num
    cache[1]=1

    for i in range(2,len(num)+1):
        cache[i]=cache[i-1]+cache[i-2]
    return cache[num]

if __name__ == '__main__':
    print(fibonacci(9))