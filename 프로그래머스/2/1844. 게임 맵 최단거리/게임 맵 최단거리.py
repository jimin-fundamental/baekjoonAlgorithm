from collections import deque

def solution(maps):
    행 = len(maps)
    열 = len(maps[0])
    dx = [0, 0, -1, +1]  # 상하좌우
    dy = [+1, -1, 0, 0]
    
    q = deque()
    visited = [[False] * 열 for _ in range(행)]
    
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for m, n in zip(dx, dy):
            nx = x + m
            ny = y + n
            if 0 <= nx < 행 and 0 <= ny < 열:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    
    return maps[행 - 1][열 - 1] if maps[행 - 1][열 - 1] != 1 else -1
