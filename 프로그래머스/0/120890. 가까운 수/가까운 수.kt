import kotlin.math.*

class Solution {
    fun solution(array: IntArray, n: Int): Int {
        var answer = 0
        
        var sub = Int.MAX_VALUE / 2
        for (i in 0..array.size-1){
            if( (abs(array[i] - n) < sub) || ( (abs(array[i] - n) == sub) && answer > array[i]) ){
                answer = array[i]
                sub = abs(array[i] - n)
            }
            
        }
     return answer   
    }
}