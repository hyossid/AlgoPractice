
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y]==0:
        graph[x][y]=1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True         # 만약 이 IF문안에 함수가 들어왔다는 뜻은, 일단 돌고있다는 뜻이니까, 한번의 if 문안에 한번의 return True 는 맞음
    return False

if __name__ == '__main__':
    n,m=map(int,input().split())  # 공백을 기준으로 맵의 크기를 입력받았다.
    graph=list()
    for i in range(n):
        graph.append(list(map(int,input())))  # Always have to make it as a list when we want to iterate
    result=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1

    print(result)