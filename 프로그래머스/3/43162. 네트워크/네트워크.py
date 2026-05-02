from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False]*n
    
    q = deque()
    
    for k in range(n):
        if not visited[k]:
            q.append(k)
            visited[k] = True
            answer += 1
            
        while q:
            cur = q.popleft()

            # cur와 연결된 거 모두 추가 
            for i in range(n):
                if computers[cur][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
    
    return answer