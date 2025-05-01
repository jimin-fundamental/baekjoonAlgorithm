import sys


def solution(nodeinfo):
    sys.setrecursionlimit(10**5)  # 수동으로 트리의 깊이 제한 늘리기
    if len(nodeinfo) == 1:
        return [[1], [1]]

    # (x,y node_id)로 변환
    nodes = [(x,y,i+1) for i, (x,y) in enumerate(nodeinfo)]
    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    # Node 클래스 정의
    class Node:
        def __init__(self, x,y,idx):
            self.x = x
            self.y = y
            self.idx = idx
            self.left = None
            self.right = None
            
    #이진 트리 삽입함수
    def insert(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                insert(parent.right,child)
    #순회함수
    def preorder(node,path):
        if node:
            path.append(node.idx)
            preorder(node.left,path)
            preorder(node.right,path)
    def postorder(node,path):
        if node:
            postorder(node.left,path)
            postorder(node.right,path)
            path.append(node.idx)
    #트리 생성
    root = Node(*nodes[0])
    for node in nodes[1:]:
        insert(root, Node(*node))
        
    #순회 결과
    pre_res, post_res = [], []
    preorder(root, pre_res)
    postorder(root, post_res)
    
    return[pre_res, post_res]
                