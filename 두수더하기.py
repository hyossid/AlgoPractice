def solution(numbers):
    tempdict = collection.defaultdict(list)

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sum = numbers[i] + numbers[j]
            tempdict[''.join(sum)]
    answer = list(tempdict)
    answer = []
    return answer


if __name__ == '__main__':