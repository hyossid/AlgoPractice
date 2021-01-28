def solution(answers):
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    temp = []
    for v in p:
        k = len(answers) // len(v) + 1
        temp.append(v * k)
    score = [[] for _ in range(len(p))]

    # Answers 를 돌면서 하나씩 체크
    for i in range(len(answers)):
        # Answer 마다 구성원의 답 체크
        for j in range(len(temp)):  # 닝겐들
            if answers[i] == temp[j][i]:
                score[j] += 1

    print(score)
    return len(temp)


if __name__ == '__main__':
    solution([1,2,3,4,5])