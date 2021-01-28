import collections


def check(word1, word2):
    l1 = list(word1)
    l2 = list(word2)
    cnt = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            continue
        else:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    # 거리가 담길 딕셔너리
    destdict = collections.defaultdict()
    # 방문한 단어가 담길 배열
    visited = list()
    Q=collections.deque()

    Q.append((begin,0))
    destdict[begin]=0
    visited.append(begin)
    while Q:
        if len(visited)==len(words)+1:
            break
        cur,dest=Q.popleft()
        for v in words:
            if check(cur,v) and v not in visited:
                destdict[v]=dest+1
                Q.append((v,dest+1))
                visited.append(v)
            else:
                continue

    if target in destdict:
        return destdict[target]
    else:
        return 0


    # # word 를 순회하면서
    # def search(node, num):
    #     if node == target:
    #         return num
    #     for v in words:
    #         if check(v, node) and v not in visited:
    #             num += 1
    #             dest[v] = num
    #             visited.append(v)
    #             search(v, num)
    #         else:
    #             continue
    #     if len(visited)==len(words)+1:
    #         return









if __name__ == '__main__':
    print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))