class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        
        for(i in citations.size downTo 1){
            if ( i <= citations.count {it >= i}) return i   
        }
        
        return answer
    }
}