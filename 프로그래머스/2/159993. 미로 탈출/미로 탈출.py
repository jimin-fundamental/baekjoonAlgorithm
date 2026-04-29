from collections import deque 

def solution(maps):
    answer = 0
    
    m = len(maps)
    n = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 출발점 -> 레버 -> 도착점
    g = [0, 0, 0]
    for r in range(m):
        for c in range(n):
            # 출발점 
            if maps[r][c] == "S":
                g[0] = (r, c)
                
            # 레버
            if maps[r][c] == "L":
                g[1] = (r, c)
            
            # 도착점
            if maps[r][c] == "E":
                g[2] = (r, c)
    
    didArrive = True
    
    for k in range(2):
        
        if not didArrive:
            return -1
        
        didArrive = False
        
        q = deque()
        
        visited = [[False]*n for _ in range(m)] 
        count = 0
        
        fy, fx = g[k]
        q.append((fy, fx, count))
        gy, gx = g[k+1]
        
        while q:
            y,x, count = q.popleft()
            
            # 도착 
            if y == gy and x == gx:
                didArrive = True
                answer += count
                break

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                # 갈 수 있는 경로 모두 추가
                if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and maps[ny][nx] != "X":
                    visited[ny][nx] = True
                    q.append((ny, nx, count+1))    
        
    
    return -1 if not didArrive else answer