def solution(n, wires):
    diff = []
    
    def dfs(node, graph, visited):
        visited[node] = True
        count = 1
        for n in graph[node]:
            if not visited[n]:
                count += dfs(n,graph, visited)
        return count
    
    #인접리스트로 표시
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    #전선 하나 끊기
    for i in range(len(wires)):
        temp_graph = [row[:] for row in graph] #깊은복사
        
        a,b = wires[i] #끊을 전선
        
        #전선 끊기
        temp_graph[a].remove(b)
        temp_graph[b].remove(a)
        
        #한쪽 노드 개수 세기
        visited = [False]*(n+1)
        tree1 = dfs(a, temp_graph, visited)
        tree2 = n- tree1
        diff.append(abs(tree1-tree2))
        
    return min(diff)
        