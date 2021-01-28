
class Edge:
    def __init__(self,node1,node2,distance):
        self.node1=node1
        self.node2=node2
        self.distance=distance

def getParent(helptable,x):
    if helptable[x]==x:
        return x
    return getParent(helptable,helptable[x])

def unionParent(helptable,a,b):
    a=getParent(helptable,a)
    b=getParent(helptable,b)
    if(a<b):
        helptable[b]=a
    else:
        helptable[a]=b

def find(helptable,a,b):
    a=getParent(helptable,a)
    b=getParent(helptable,b)
    if a==b:
        return 1
    else:
        return 0


if __name__ == '__main__':
    graph=list()
    graph.append(Edge(1,7,12))
    graph.append(Edge(1,4,28))
    graph.append(Edge(1,2,67))
    graph.append(Edge(1,5,17))
    graph.append(Edge(2,4,24))
    graph.append(Edge(2,5,62))
    graph.append(Edge(3,5,20))
    graph.append(Edge(3,6,37))
    graph.append(Edge(4,7,13))
    graph.append(Edge(5,6,45))
    graph.append(Edge(5,7,73))

    graph.sort(reverse=True,key=lambda edge:edge.distance)

    helptable=[0]*len(graph)
    #초기에는 모두 부모 1 (노드마다 각기 다른 그래프로 해석)
    for i in range(len(graph)):
        helptable[i]=i

    sum =0
    for v in graph:
        if find(helptable,v.node1,v.node2) ==0:
            sum+=v.distance
            unionParent(helptable,v.node1,v.node2)




