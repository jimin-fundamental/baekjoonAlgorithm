def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        min_dist = float('inf')
        # 1) 왼쪽 벽 (x = 0)에 반사
        # 조건: startY == y 이고 목표공이 왼쪽(startX보다 작은 x)에 있으면 skip
        if not (startY == y and x < startX):
            dx = startX + x                # startX - (-x) = startX + x
            dy = startY - y
            min_dist = min(min_dist, dx*dx + dy*dy)

        # 2) 오른쪽 벽 (x = m)에 반사
        # 조건: startY == y 이고 목표공이 오른쪽(startX보다 큰 x)에 있으면 skip
        if not (startY == y and x > startX):
            dx = (2*m - startX - x)        # (2*m - x) - startX
            dy = startY - y
            min_dist = min(min_dist, dx*dx + dy*dy)

        # 3) 아래쪽 벽 (y = 0)에 반사
        # 조건: startX == x 이고 목표공이 아래(startY보다 작은 y)에 있으면 skip
        if not (startX == x and y < startY):
            dx = startX - x
            dy = startY + y                # startY - (-y) = startY + y
            min_dist = min(min_dist, dx*dx + dy*dy)

        # 4) 위쪽 벽 (y = n)에 반사
        # 조건: startX == x 이고 목표공이 위(startY보다 큰 y)에 있으면 skip
        if not (startX == x and y > startY):
            dx = startX - x
            dy = (2*n - startY - y)        # (2*n - y) - startY
            min_dist = min(min_dist, dx*dx + dy*dy)

        answer.append(min_dist)

    return answer
