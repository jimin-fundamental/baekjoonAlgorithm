from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 이동 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append((0, 0))  # 시작점 (0,0)

    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 벽이면 무시
            if maps[nx][ny] == 0:
                continue
            
            # 처음 가는 길이면 거리 저장 및 큐에 추가
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    # 상대 팀 진영에 도착했는지 확인
    if maps[n-1][m-1] == 1:
        return -1  # 도착 못함
    else:
        return maps[n-1][m-1]
