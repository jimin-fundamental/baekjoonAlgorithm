from collections import deque

def solution(n, computers):
    group = [0]*n #0이면 아직 그룹 없음, 1.2.3... 각 그룹
    count = 0
    
    # 연결되어있는지 체크하는 함수
    def dfs(current_node):
        nonlocal count
        q = deque([current_node])
        count += 1
        nowGroup = count #현재그룹번호
                
        #같은 그룹과 연결된 것끼리 DFS 수행
        while q:
            node = q.pop()
            # 이미 방문한 노드면 건너뛰기
            if group[node] != 0:
                continue
            group[node] = nowGroup
            for i in range(n):
                if computers[node][i] == 1 and group[i] ==0:
                    q.append(i)
    
    for i in range(n):  # 모든 노드에 대해 dfs 시도
        if group[i] == 0:
            dfs(i)
    return count