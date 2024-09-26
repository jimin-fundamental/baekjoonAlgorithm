def solution(board):
    answer = 0
    height = len(board)
    width = len(board[0])
    
    dp = [
        [0 for _ in range(width)]
        for _ in range(height)
    ]
    
    # dp 배열의 첫 행과 열은 복붙
    for i in range(width):
        dp[0][i] = board[0][i]
        answer = max(dp[0][i], answer)
    for i in range(height):
        dp[i][0] = board[i][0]
        answer = max(dp[i][0], answer)
        
    # dp 사용해서 계산
    for m in range(1, height):
        for n in range(1, width):
            if board[m][n] == 1:
                dp[m][n] = min(dp[m][n-1], dp[m-1][n], dp[m-1][n-1]) + 1
                answer = max(dp[m][n], answer)
                
    answer = answer ** 2

    return answer