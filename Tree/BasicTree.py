

class Node:
    def __init__(self,data,leftnode,rightnode):
        self.data=data
        self.leftnode=leftnode
        self.rightnode=rightnode

def preorder(node):
    print(node.data,end=" ")
    if node.leftnode!=None:
        preorder(tree[node.leftnode])
    if node.rightnode!=None:
        preorder(tree[node.rightnode])

if __name__ == '__main__':

    n=int(input())  ## Dimension of Tree (Number of Nodes in Tree)
    tree={}

    for i in range(n):
        data,leftnode,rightnode=input().split()
        if leftnode=="None":
            leftnode=None
        if rightnode=="None":
            rightnode=None
        tree[data]=Node(data,leftnode,rightnode)

    preorder(tree['A'])


