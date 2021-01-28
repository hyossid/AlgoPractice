"""

    입력이 루트노드 하나로 들어온다. 이때 입력이 루트노드 하나이더라도 다 연결되어있으니까 트리라고 볼 수 있다.
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root:TreeNode):
    pass



if __name__ == '__main__':
    root=[2,3,4]
    queue=collections.deque([root])
    queue.append([3,4])

    print(queue)