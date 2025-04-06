from collections import deque

# 4방향 이동 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 테두리(모서리)인지 판단하는 함수
def is_border(x, y, rects):
    if rects[y][x] != 1:
        return False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if rects[y + i][x + j] == 0:
                return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 확장을 위한 102x102 맵
    grid = [[0] * 102 for _ in range(102)]

    # 사각형 내부 채우기 (2배 확장)
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1 * 2, y2 * 2 + 1):
            for x in range(x1 * 2, x2 * 2 + 1):
                grid[y][x] = 1

    # 테두리만 탐색 가능하도록 설정
    borders = [[0] * 102 for _ in range(102)]
    for y in range(1, 101):
        for x in range(1, 101):
            if is_border(x, y, grid):
                borders[y][x] = 1

    # BFS
    visited = [[False] * 102 for _ in range(102)]
    q = deque()
    start_x, start_y = characterX * 2, characterY * 2
    end_x, end_y = itemX * 2, itemY * 2

    q.append((start_x, start_y, 0))
    visited[start_y][start_x] = True

    while q:
        x, y, dist = q.popleft()
        if (x, y) == (end_x, end_y):
            return dist // 2  # 2배 확장 좌표 → 거리 절반이 실제 거리

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visited[ny][nx] and borders[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny, dist + 1))
