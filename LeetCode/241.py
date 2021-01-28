"""

부차적인 재귀속 results 에는 계속 중간값들이 담기며, return 하여 left right dp emfdjrkrh

최종 result 에만 관심있게된다.
"""

def compute(left,right,op):
    # left / right 에는 이전 결과의 연산의 결과로서 가능한 값들이 들어가게된다.
    results=[]
    for l in left:
        for r in right:
            results.append(eval(str(l)+op+str(r)))

    return results


def solution(inputs):

    if inputs.isdigit():
        return [int(inputs)]

    results=[]
    for index,value in enumerate(inputs):
        if value in "+-*":
            # left / right 에 아래단계 재귀에서의 연산의 결과가 담기게된다.
            left=solution(inputs[:index])
            right=solution(inputs[index+1:])

            results.extend(compute(left,right,value))
    return results




if __name__ == '__main__':
    print(solution("2*3-4*5"))