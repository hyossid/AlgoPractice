def solution(number, k):
    answer = ''
    results = []
    numbers = list(number)

    def combination(elements,index):
        if len(elements)==len(numbers)-k:
            results.append(elements[:])
            return
        for i in range(index,len(numbers)):
            nextelements=elements[:]
            nextelements.append(numbers[i])
            combination(nextelements,i+1)
            #nextelements.pop() # 어차피 인덱스 때문에 이거는 데드코드가 되버리는구나....

    combination([],0)
    return results


if __name__ == '__main__':
    print(solution("1924",2))