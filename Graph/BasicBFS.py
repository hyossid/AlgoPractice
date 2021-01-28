
"""

    BFS
    Queue 를사용해서
    하나씩 넣었음
    (1,1) 이 시작지점이다.
"""
from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx
            ny=y+dy
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            else:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1

    return graph[n-1][m-1]


if __name__ == '__main__':
    n,m=map(int,input().split())

    graph=[]
    for i in range(n):
        graph.append(list(map(int,input())))

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    print(bfs(0,0))