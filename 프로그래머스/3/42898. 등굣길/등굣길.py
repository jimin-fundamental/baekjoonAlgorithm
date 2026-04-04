"""
격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles
오른쪽과 아래쪽으로만 움직일 수 있음 -> DP
집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지
"""
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # dp 초기화하기
    for dy in range(1, n+1):
        for dx in range(1, m+1):
            if dy== 1 and dx == 1:
                dp[dy][dx] = 1
            elif [dx, dy] not in puddles:
                dp[dy][dx] = dp[dy][dx-1]+dp[dy-1][dx]
    
    return dp[n][m] % 1000000007
                
            