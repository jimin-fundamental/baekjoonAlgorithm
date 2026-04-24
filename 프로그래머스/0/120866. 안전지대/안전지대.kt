class Solution {
    fun solution(board: Array<IntArray>): Int {
        var answer: Int = 0
        val n = board.size
        
        for(i in 0 until n){
            for (j in 0 until n){
                if(board[i][j] == 1){
                    if(i-1 >= 0){
                        if(board[i-1][j] == 0) board[i-1][j] = 2
                        if(j-1 >= 0){
                            if(board[i-1][j-1] == 0) board[i-1][j-1] = 2
                        }
                        if(j+1 < n){
                            if(board[i-1][j+1] == 0) board[i-1][j+1] = 2
                        }
                        
                    }
                    if(i+1 < n){
                        if(board[i+1][j] == 0) board[i+1][j] = 2
                        if(j-1 >= 0){
                            if(board[i+1][j-1] == 0) board[i+1][j-1] = 2
                        }
                        if(j+1 < n){
                            if(board[i+1][j+1] == 0) board[i+1][j+1] = 2
                        }
                        
                    }
                    if(j-1 >= 0){
                        if(board[i][j-1] == 0) board[i][j-1] = 2
                    }
                    if(j+1 < n){
                        if(board[i][j+1] == 0) board[i][j+1] = 2
                    }
                    
                }
            }
        }
         for(i in 0 until n){
            for (j in 0 until n){
                if(board[i][j] == 0) answer++
            }
         }
        
        
        
        return answer
    }
}