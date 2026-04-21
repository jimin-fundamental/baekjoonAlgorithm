class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray 
        var odd = 0
        var even = 0
        for(num in num_list){
            if(num % 2 == 0) even += 1
            else odd += 1
        }
        answer = intArrayOf(even, odd)
        return answer
    }
}