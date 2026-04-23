class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        // 콜라 
        var answer: Int = 0
        
        // 빈 병
        var count = n
        
        while(count >= a){
            var new_coke = (count / a)*b
            
            answer += new_coke
            
            // 콜라 바꾸고 남은 빈병 + 새로 받은 콜라로 만든 빈병
            count = count % a + new_coke
        }
        
        return answer 
    }
}