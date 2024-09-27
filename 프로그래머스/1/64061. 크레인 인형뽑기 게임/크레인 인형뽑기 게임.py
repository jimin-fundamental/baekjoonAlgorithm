def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []

    for move in moves:
        move = move -1
        for i in range(n):
            if board[i][move] != 0:
                doll = board[i][move]
                board[i][move] = 0
                if stack and stack[-1] == doll:
                    #터뜨리기
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                break                
        
    return answer