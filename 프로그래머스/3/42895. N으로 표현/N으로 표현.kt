class Solution {
    fun solution(N: Int, number: Int): Int {
        // dp[2] = N 2개로 만들 수 있는 숫자의 경우 <- dp[1] 사칙연산 + N 2개 이어붙인 수 
        val dp = Array(9){mutableSetOf<Int>()}
        
        if(N == number) return 1
        
        for(i in 1..8){
            dp[i].add(N.toString().repeat(i).toInt())
            
            for(j in 1 until i){
                val left = dp[j]
                val right = dp[i-j]
                
                for(a in left){
                    for(b in right){
                        dp[i].add(a + b)
                        dp[i].add(a - b)
                        dp[i].add(a * b)
                        if(b != 0) dp[i].add(a / b)
                    }
                } 
            }
            if(number in dp[i]) return i
        }
        return -1
    }
}