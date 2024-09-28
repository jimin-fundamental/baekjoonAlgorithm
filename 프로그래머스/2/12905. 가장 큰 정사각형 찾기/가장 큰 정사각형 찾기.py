def solution(board):
    answer = 0
    
    height = len(board)
    width = len(board[0])
    
    dp = [[0]*width for _ in range(height)]
    
    
    #첫행열
    for h in range(height):
        dp[h][0] = board[h][0]
        answer = max(answer, dp[h][0])
    
    for w in range(width):
        dp[0][w] = board[0][w]
        answer = max(answer, dp[0][w])
        
    # 나머지 계산
    for h in range(1, height):
        for w in range(1, width):
            if board[h][w] == 1:
                dp[h][w] = min(dp[h-1][w-1], dp[h][w-1], dp[h-1][w]) +1
                answer = max(answer, dp[h][w])
        
    answer = answer ** 2

    return answer