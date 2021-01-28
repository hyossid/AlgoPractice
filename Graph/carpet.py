def solution(brown, yellow):
    answer = []
    sums = brown + yellow
    # ans1, ans2 의 곱이 sums가 되야함
    cand = []
    for n in range(1, sums // 2 + 1):
        if sums % n == 0:
            b = int(sums // n)
            cand.append([n,b])
    print(cand)

    for v in cand:
        a = v[0] - 2
        b = v[1] - 2
        if a * b == yellow:
            answer.append([v[0], v[1]])

    # ans1-2 * ans2-2 가 yellow 가 되야함
    return answer

if __name__ == '__main__':
    print(solution(10,2))