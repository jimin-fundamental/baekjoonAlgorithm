class Solution {
    var answer = 0
    
    fun dfs(idx: Int, sum: Int, numbers: IntArray, target: Int){
        // 종료 조건
        if(idx >= numbers.size -1){
            if(sum == target){
                answer++
            }
            return
        }
        
        
        dfs(idx+1, sum + numbers[idx+1], numbers, target)
        dfs(idx+1, sum - numbers[idx+1], numbers, target)
        
        
    }
    
    fun solution(numbers: IntArray, target: Int): Int {
        dfs(-1, 0, numbers, target)
        
        return answer
    }
}