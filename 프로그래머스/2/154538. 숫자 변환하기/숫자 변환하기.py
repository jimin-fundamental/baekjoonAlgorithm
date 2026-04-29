from collections import deque

def solution(x, y, n):
    q = deque()
    
    visited = [False] * (y+1)
    
    q.append((x, 0))
    visited[x] = True
    
    while q:
        cur, count = q.popleft()
        
        if cur == y:
            return count
        
        if cur+n <= y and not visited[cur+n]:
            visited[cur+n] = True
            q.append((cur+n, count+1))
        if cur*2 <= y and not visited[cur*2]:
            visited[cur*2] = True
            q.append((cur*2, count+1))
        if cur*3 <= y and not visited[cur*3]:
            visited[cur*3] = True
            q.append((cur*3, count+1))
        
    
    return -1