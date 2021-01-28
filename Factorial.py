


def factorial(num)->int:
    if num>0:
        ans=num*factorial((num-1))
        return num*factorial((num-1))
    else:
        return 1

if __name__ == '__main__':
    num=int(input())

    print(factorial(num))


