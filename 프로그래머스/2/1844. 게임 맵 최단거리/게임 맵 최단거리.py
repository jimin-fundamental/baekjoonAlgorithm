from collections import deque

def solution(maps):
    n = len(maps) #행
    m = len(maps[0]) #열
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0,0,-1,1]
    
    queue = deque() # 방문해야 할 좌표
    queue.append((0,0)) #시작점
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x,y = queue.popleft() # 현재 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 안에 있고, 벽이 아니고, 방문 안 했으면
            if 0 <=nx < n and 0 <= ny < m and maps[nx][ny] ==1 and not visited[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1 # 이전 칸 + 1 (거리 저장)
                visited[nx][ny] = True # 방문 처리
                queue.append((nx,ny)) # 다음 탐색을 위해 큐에 추가
    if maps[n-1][m-1] == 1:
        return -1 #아직 도달X
    else:
        return maps[n-1][m-1]