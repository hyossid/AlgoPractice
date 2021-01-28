import collections
import heapq

def dijikstra(times,N,K):
    graph=collections.defaultdict(list) # list 를 value 로 받을수있는 딕셔너리 만들었다. 그래프 용도.
    for u,w,v in times:
        graph[u].append((u,w))      # 딕셔너리에 더할때 꼭 append 쓰자! set 만 add임.
    dist=collections.defaultdict(int) # 시작점으로부터의 거리를 저장할 딕셔너리
    Q=[(0,K)]   # 튜플 (거리,도착점) 이담길 리스트 이며 heapify 할것임.
    heapq.heapify(Q)
    while Q:
        x,node=heapq.heappop(Q)
        if node not in dist:
            dist[node]=x
            for u,w in graph[node]: # node와 연결되어있는 모든 점에 대해서
                alt=x+w
                heapq.heappush(Q,(alt,u))
        if len(dist)==N:
            return max(dist.values())
        else:
            return -1

if __name__ == '__main__':
    times=[[2,1,1],[2,3,1],[3,4,1]]
    N=4
    K=2
    graph=collections.defaultdict(list)
    # Make Graph
    for u,v,w in times:
        graph[u].append((v,w)) # 그래프를 딕셔너리로 받는다. key는 시작점, 도착점과 distance 는 튜플로.
    Q=[(0,K)]   # 시작점
    dist=collections.defaultdict(int)   # 시작점으로부터의 거리를 저장
    while Q:
        time,node=heapq.heappop(Q)  # 걸리는 distance와 도착지점 가장가까운놈!
        if node not in dist:    # 큐에서 팝한 점이 도착하지 않은점이라면,
            dist[node]=time # 걸린 시간을 넣어준다.
            for v,w in graph[node]: # 노드와 연결되어있는 점들과 그 거리에 대해서
                alt=time+w  # 걸린시간을 더해주고
                heapq.heappush(Q,(alt,v))   # 다시 우선순위큐에 넣어준다.
    if len(dist)==N: # 다 도착했으
        print(max(dist.values()))
    else:
        print("-1")