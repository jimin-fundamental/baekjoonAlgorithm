def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur):
        nonlocal answer
        
        visited[cur] = True
        
        for next in range(n):
            if cur != next and not visited[next] and computers[cur][next] == 1:
                    dfs(next)
            
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer