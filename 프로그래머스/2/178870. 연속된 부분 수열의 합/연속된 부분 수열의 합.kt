class Solution {
    fun solution(sequence: IntArray, k: Int): IntArray {
        var left = 0
        var right = 0
        var sum = sequence[0]
        
        var bestStart = 0
        var bestEnd = sequence.size - 1
        var bestLength = sequence.size
        
        while(left < sequence.size && right < sequence.size){
            when{
                sum == k -> {
                    val length = right - left
                    
                    if(length < bestLength){
                        bestLength = length
                        bestStart = left
                        bestEnd = right
                    }
                    
                    // 다음 후보를 보기 위해 왼쪽을 줄임
                    sum -= sequence[left]
                    left++
                }
                
                sum > k -> {
                    // 현재 left는 sum에 포함되어 있고 그걸 제거해야 함
                    sum -= sequence[left]
                    left++
                }
                
                sum < k -> {
                    // 현재 right는 sum에 포함되어 있고, 그 다음 인덱스를 추가해줘야 됨. 
                    right++
                    
                    if(right < sequence.size){
                        sum += sequence[right]
                    }
                    
                    
                }
            }
        }
        
        return intArrayOf(bestStart, bestEnd)
        
    }
}