class Solution {
    fun solution(a: IntArray): Int {
        val n = a.size
        
        if(n <= 2) return n
        
        val leftMin = IntArray(n)
        val rightMin = IntArray(n)
        
        leftMin[0] = a[0]
        
        for(i in 1 until n){
            leftMin[i] = minOf(leftMin[i-1], a[i])
        }
        
        rightMin[n-1] = a[n-1]
        
        for(i in n-2 downTo 0){
            rightMin[i] = minOf(rightMin[i+1], a[i])
        }
        
        var answer = 0
        
        for(i in 0 until n){
            if (a[i] <= leftMin[i] || a[i] <= rightMin[i]){
                answer++
            }
        }
        
        return answer
    }
}