"""
지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY
캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return -> BFS
"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1) 직사각형을 좌표로 표현
    net = [[0]*102 for _ in range(102)]
    
    for dx1, dy1, dx2, dy2 in rectangle:
        dx1, dy1, dx2, dy2 = dx1*2 , dy1*2, dx2*2, dy2*2
        # 테두리 모두 1로 표시
        for dy in range(dy1, dy2+1):
            for dx in range(dx1, dx2+1):
                net[dy][dx] = 1

    for dx1, dy1, dx2, dy2 in rectangle:
        dx1, dy1, dx2, dy2 = dx1*2 , dy1*2, dx2*2, dy2*2
        # 내부 중에 1인 거 모두 0으로 표시
        for dy in range(dy1+1, dy2):
            for dx in range(dx1+1, dx2):
                if net[dy][dx] == 1:
                    net[dy][dx] = 0
    
    # 2) bfs로 최단경로 구하기
    q = deque([(characterY*2, characterX*2, 0)])
    visited = [[0]*102 for _ in range(102)] #0이 방문 X
    visited[characterY*2][characterX*2] = 1
    
    while q:
        cy, cx, count = q.popleft()
        
        # 다음 좌표는 y에 1 더하거나 빼거나 or x에 1 더한 거나 빼거나
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 1 <= ny <= 100 and 1 <= nx <= 100 and net[ny][nx] == 1 and visited[ny][nx] == 0:
                
                # 종료 조건 체크 
                if ny == itemY*2 and nx == itemX*2:
                    return (count+1) // 2
                
                # 종료되지 않았으면 이를 기준으로 더 가기 
                visited[ny][nx] = 1
                q.append((ny, nx, count +1))
    

                
            