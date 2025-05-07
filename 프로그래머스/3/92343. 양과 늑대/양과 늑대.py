from collections import defaultdict

def solution(info, edges):
    #1. 인접리스트로 부모 자식 연결 
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    max_sheep = 0
    # 2. 리스트 읽으면서 양/늑대 기록해보기 - DFS
    def dfs(sheep, wolf, possible_next_nodes):
        nonlocal max_sheep
        max_sheep = max(max_sheep, sheep)
        for i, p in enumerate(possible_next_nodes):
            new_sheep = sheep
            new_wolf = wolf
            
            if info[p] == 0:
                new_sheep += 1
            else:
                new_wolf += 1
            
            if new_sheep <= new_wolf:
                continue #양이 잡아먹히므로 이 경로는 pass!
            
            # 다음 방문 후보 리스트 구성(현재 후보들 중 이번 node 제외 + 자식 추가)
            next_nodes = possible_next_nodes[:i]+possible_next_nodes[i+1:]
            next_nodes += graph[p]
            
            dfs(new_sheep, new_wolf, next_nodes)
                
    dfs(1, 0, graph[0]) # 루트는 양이니까 sheep=1부터 시작
    
    return max_sheep
        