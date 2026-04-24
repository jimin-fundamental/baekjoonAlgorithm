import kotlin.math.*

class Solution {
    fun gcd(a: Int, b: Int): Int {
        var x = max(a,b)
        var y = min(a,b)
        
        while(y != 0){
            var temp = x % y
            x = y
            y = temp
        }
        
        return x
    }
    
    fun solution(a: Int, b: Int): Int {
        var n = gcd(a,b)
        
        var curb = b / n
        
        // curb의 소인수가 2와 5만 존재하는지 체크 
        while (curb % 2 == 0){
            curb = curb / 2
        }
        while (curb % 5 == 0){
            curb = curb / 5
        }
        
        if(curb == 1) return 1
        else return 2
    }
}