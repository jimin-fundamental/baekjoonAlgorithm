class Solution {
    fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
        val INF = Int.MAX_VALUE / 2
        
        // B 흔적이 b일 때 가능한 최소 A 흔적
        var dp = IntArray(m) {INF}
        
        // 아무것도 훔치지 않았을 때
        dp[0]= 0   
        
        // 물건 하나씩 처리
        for (item in info) {
            val aTrace = item[0]
            val bTrace = item[1]
            
            // 이번 물건을 반영한 다음 상태 배영
            val next = IntArray(m) {INF}
            
            for(b in 0 until m){
                if(dp[b] == INF) continue
                
                // A가 이 물건을 훔치는 경우
                val nextA = dp[b] + aTrace
                
                if(nextA < n){
                    // B는 변화 없음 -> b 그대로
                    // A 흔적 최솟값 갱신
                    next[b] = minOf(next[b], nextA)
                }
                
                // B가 훔치는 경우
                val nextB = b + bTrace
                
                if (nextB < m){
                    // A는 변화 없음 -> dp[b]
                    // B 흔적이 nextB일 때 A 최솟값 갱신
                    next[nextB] = minOf(next[nextB], dp[b])
                }
                 
            }
            
            dp = next
            
            
            
        }
        
        val answer = dp.minOrNull() ?: INF
        
        
        return if (answer == INF) -1 else answer
    }
}