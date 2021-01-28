from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()

    while people:
        if len(people)==1 or len(people)==0:
            answer += 1
            return answer
        else:
            if people[0] + people[1] <= 100:
                answer += 1
                people.pop(0)
                people.pop(0)
            else:
                answer += len(people)
                return answer

    return answer


if __name__ == '__main__':
    print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1],100))