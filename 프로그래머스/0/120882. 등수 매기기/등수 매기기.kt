class Solution {
    fun solution(score: Array<IntArray>): IntArray {
        var answer= mutableListOf<Int>()
        
        val avg = score.map {(it[0] + it[1]) / 2.toDouble()}
        val sorted = avg.sortedDescending()
        
        for(a in avg){
            answer.add(sorted.indexOf(a)+1)
        }
        
        
        return answer.toIntArray()
    }
}