


class Node:
    def __init__(self,value):
        self.value=value
        self.leftnode=None
        self.rightnode=None

class NodeMgmt:
    def __init__(self,head):
        self.head=head
    def insert(self,value):
        self.current_node=self.head
        while True:
            if value<self.current_node:
                if self.current_node.leftnode!=None:
                    self.current_node=self.current_node.leftnode
                else:
                    self.current_node.leftnode=Node(value)
            else:
                if self.current_node.rightnode != None:
                    self.current_node = self.current_node.rightnode
                else:
                    self.current_node.rightnode = Node(value)
    def search(self,value):
        self.current_node=head
        while self.current_node:
            if self.current_node==value:
                return True
            elif self.current_node>value:
                self.current_node=self.current_node.leftnode
            else:
                self.current_node=self.current_node.rightnode
            return False

    # 이진트리의 삭제
    def delete(self,value):
        searched = False
        self.current_node=self.head
        self.parent=self.head
        while self.current_node:
            if self.current_node.value==value:
                searched=True
                break
            elif value < self.current_node.value:
                self.current_node=self.current_node.leftnode
            else:
                self.current_node=self.current_node.rightnode
        if searched==False:
            return False

        # 만약 Leaf node 일경우
        if self.current_node.leftnode==None and self.current_node.rightnode=None:
            if value<self.parent.value:
                self.parent.leftNode=None
            else:
                self.parent.rightnode=None

        # 만약 Child Node 한개를 가지고 있을때
        if self.current_node.leftnode!=None and self.current_node.rightnode==None:
            if value<self.parent.value:
                self.parent.leftnode=self.current_node.leftnode
            else:
                self.parent.rightnode=self.current_node.rightnode
        elif self.current_node.left==None and self.current_node.right!=None:
            if value>self.parent.value:
                self.parent.leftnode=self.current_node.leftnode
            else:
                self.parent.rightnode=self.current_node.rightnode
        # 만약 Child Node 두개를 가지고 있고, parent 왼쪽에 있을때
        if self.current_node.leftnode!=None and self.current_node.right!=None:
            if value<self.parent.value:
                self.change_node=self.current_node.right
                self.change_node_parent=self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent=self.change_node
        # 만약 Child Node 두개를 가지고 있고, parent 오른쪽에 있을때
if __name__ == '__main__':
    head=Node(1)
    binary_tree=NodeMgmt(head)