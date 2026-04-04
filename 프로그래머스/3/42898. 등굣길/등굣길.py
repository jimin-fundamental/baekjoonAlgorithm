"""
격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles
오른쪽과 아래쪽으로만 움직일 수 있음 -> DP
집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지
"""
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    dp[1][1] = 0
    
    # 제일 바깥쪽 위랑 왼쪽 테두리 1로 초기화
    for y in range(2, n+1):
        # 만약 앞이 puddle이면 거기부터 끝까지 0으로 초기화해야 함
        if [1, y] not in puddles: #puddles는 문제에서 주는 걸로 반대로 들어가 있음 <- 주의!
            dp[y][1] = 1
        else:
            break
    for x in range(2, m+1):
        if [x, 1] not in puddles:
            dp[1][x] = 1
        else:
            break
    
    # dp 초기화하기
    for dy in range(2, n+1):
        for dx in range(2, m+1):
            if [dx, dy] in puddles:
                dp[dy][dx] = 0
            else:
                dp[dy][dx] = dp[dy][dx-1]+dp[dy-1][dx]
    
    return dp[n][m] % 1000000007
                
            