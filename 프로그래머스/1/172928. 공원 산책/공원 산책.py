def solution(park, routes):
    park_map = []
    start_x, start_y = 0, 0  # 시작 위치 초기화

    # 공원을 2차원 배열로 만들면서 시작 위치(S) 찾기
    for i, row in enumerate(park):
        new_row = []
        for j, cell in enumerate(row):
            new_row.append(cell)
            if cell == "S":
                start_x, start_y = i, j  # 시작 위치 저장
        park_map.append(new_row)

    # 방향 이동 정의
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    # 명령 실행
    for r in routes:
        dir, step = r.split()
        dx, dy = direction[dir]
        step = int(step)

        nx, ny = start_x, start_y
        valid = True

        # 한 칸씩 이동하며 유효한지 검사
        for _ in range(step):
            nx += dx
            ny += dy
            # 범위 벗어나거나 장애물이면 명령 무시
            if not (0 <= nx < len(park_map) and 0 <= ny < len(park_map[0])):
                valid = False
                break
            if park_map[nx][ny] == "X":
                valid = False
                break

        # 이동 가능하면 위치 업데이트
        if valid:
            start_x, start_y = nx, ny

    return [start_x, start_y]
