from collections import deque

def solution(n, edge):
    
    # 1번 노드부터 각 노드까지의 거리를 저장 
    distances = [-1 for _ in range(n+1)]
    distances[1] = 0
    
    # edge 그래프(인접리스트) 만들기
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # BFS에서 방문 예정인 노드 담기 
    q = deque([1])
    
    while q:
        cur = q.popleft()
        for neighbor in graph[cur]:
            if distances[neighbor] == -1:
                q.append(neighbor)
                distances[neighbor] = distances[cur] + 1
    
    
    
    most_far = max(distances)
    
    return distances.count(most_far)
        
        
    