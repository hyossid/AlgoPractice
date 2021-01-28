

def solutions(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) -1
    return answer



if __name__ == '__main__':
    clothes=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ["green_turban", "headgear"]]
    print(solutions(clothes))

