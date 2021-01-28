import collections


def solution(tickets):
    answer = []
    nodes = []
    results = []  # 가능한 경로가 담길 리스트, 알파벳 순으로 가장 작은걸 리턴한다.
    cticket = tickets[:]
    for v in tickets:
        if v[0] not in nodes:
            nodes.append(v[0])
        if v[1] not in nodes:
            nodes.append(v[1])
    # cticket 과 nodes
    start = "ICN"

    def dfs(cur, lst,element):
        if len(element) == 0:
            temp=[]
            for i in range(len(lst)):
                if i==0:
                    temp.append(lst[i][0])
                    temp.append(lst[i][1])
                else:
                    temp.append(lst[i][1])
            results.append(temp)
            return
        for v in element:
            if v[0] == cur:
                nexts=element[:]
                nexts.remove(v)
                lst.append(v)
                dfs(v[1], lst,nexts)
                lst.pop()

    dfs(start, [],cticket)

    for v in results:
        if v[0]!=start:
            results.remove(v)
    results.sort()
    return results





if __name__ == '__main__':
    #print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    #print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))