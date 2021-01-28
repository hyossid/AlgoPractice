
def dfs(x,y):
    if x<=-1 or x>=4 or y<=-1 or y>=5:
        print("fucked")
        return
    elif target[x][y]==0 and graph[x][y]==1:       # 이거 안달면 이미 방문했던 0,0을 다시건들이는거임 무한재귀
        target[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return
    return

if __name__ == '__main__':
    # n,m=map(int,input().split())
    # graph=[]
    # for i in range(n):
    #     graph.append(list(input()))
    graph=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,1,0,1]]
    target=[[0]*5 for _ in range(4)]    # 오 좋은 기술이다.
    cnt=0
    for i in range(4):
        for j in range(5):
            if target[i][j]==0 and graph[i][j]==1:
                dfs(i,j)
                cnt+=1
            else:
                continue

    print(cnt)