def solution(array, commands):
    answer = []
    for v in commands:
        lst = array[v[0]-1:v[1]]
        lst.sort()
        j=v[2]
        answer.append(lst[j-1])

    return answer


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))