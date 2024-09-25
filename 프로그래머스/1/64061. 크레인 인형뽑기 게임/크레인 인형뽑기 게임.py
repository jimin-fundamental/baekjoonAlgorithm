def solution(board, moves):
    answer = 0 #사라진 인형의 수
    basket = [] 
    #집어서 올려서 basket에 넣는 거 구현
    len_board = len(board)
    #return len_board
    for move in moves:
        move = move -1
        for i in range(len_board):
            if board[i][move] != 0:
                #인형 빼고
                doll = board[i][move]
                board[i][move] = 0
                #basket 넣기 전 터지는지 확인 - pop이 오래 걸림
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                #loop 종료
                break
    
    return answer