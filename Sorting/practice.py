def crack(num):
    lst = []
    s = str(num)
    for v in s:
        lst.append(int(v))
    return lst
def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)[0])
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            lst1 = crack(numbers[i])
            lst2 = crack(numbers[j])
            score = 0
            for v in lst1:
                for w in lst2:
                    if v > w:
                        score += 1
                    else:
                        score -= 1
            if score < 0:
                t = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = t
    for v in numbers:
        answer += str(v)

    return answer