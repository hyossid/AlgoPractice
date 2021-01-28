def solution(name):
    answer = 0
    dish = ['A'] * len(name)

    for i in range(len(name)):
        if name[i]=='A':
            pass
        else:
            answer += min(ord(name[i]) - ord(dish[i-1]), ord('Z')+1-ord(dish[i-1]) + ord(name[i]))
        answer += 1
    return answer-1



if __name__ == '__main__':
    print(solution("JAN"))