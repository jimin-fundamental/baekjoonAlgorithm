def solution(n):
    def is_safe(queen_positions, row, col):
        # 이미 놓은 퀸들이 있는 위치와 새로 놓으려는 위치 (row, col)를 비교해서 안전한지 확인
        for r, c in enumerate(queen_positions[:row]):
            # 같은 열에 있거나 대각선에 위치하면 안전하지 않음
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def place_queens(queen_positions, row):
        if row == n:
            # 모든 행에 퀸을 배치했으면 성공적인 배치
            return 1
        count = 0
        for col in range(n):
            if is_safe(queen_positions, row, col):
                # 퀸을 놓을 수 있는 자리라면 배치하고, 다음 행으로 진행
                queen_positions[row] = col
                count += place_queens(queen_positions, row + 1)
        return count

    # 각 행에 놓인 퀸의 열 위치를 저장하는 리스트
    queen_positions = [-1] * n
    return place_queens(queen_positions, 0)
