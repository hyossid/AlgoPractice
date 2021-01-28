import collections
def solution(n, edge):
    # 먼저 그래프를 만들고
    # BFS 로 탐색하고 가장큰놈 리턴하면 될듯
    #graph=[[]]*n   ### 각 리스트가 같은 녀석을 레퍼런스 하는꼴이므로 이렇게하면 큰일난다.
    graph=[[i] for i in range(n+1)]
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    queue=[]
    distance=[0 for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    queue.append(graph[1])
    visited[1]=1
    while queue:
        cur=queue.pop(0)    # 리스트
        for i in range(1,len(cur)):
            if visited[cur[i]]==0: # 방문하지 않았다면
                visited[cur[i]]=1 # 방문처리 하고,
                distance[cur[i]]=distance[cur[0]]+1
                queue.append(graph[cur[i]])


    a=max(distance)
    cnt=0
    for v in distance:
        if v==a:
            cnt+=1

    return cnt



if __name__ == '__main__':
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))