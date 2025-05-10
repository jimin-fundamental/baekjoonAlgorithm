from collections import defaultdict, deque

def solution(n, edge):
    # 1. 인접리스트로 그래프 구성
    graph = defaultdict(list)
    
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [False]*(n+1)
    distance= [0]*(n+1)
    
    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current]+1
                queue.append(neighbor)
    max_dist = max(distance)
    return distance.count(max_dist)    
        
                