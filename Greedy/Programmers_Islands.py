
table=[]
def getParents(node)->int:
    if table[node]==node:
        return node
    else:
        return getParents(table[node])

def find(node1,node2)->bool:
    if getParents(node1)==getParents(node2):
        return True
    else:
        return False

def solution(n, costs):
    for i in range(n):
        table.append(i)
    costs.sort(key=lambda v:v[2])   # 오름차순으로 간선들을 정렬했다.
    sum=0
    for v in costs:
        if find(v[0],v[1])!=True:
            a = getParents(v[0])
            b = getParents(v[1])
            if a<b:
                table[b]=table[a]
            else:
                table[a]=table[b]
            sum+=v[2]
    answer=sum
    return answer



if __name__ == '__main__':
    print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))