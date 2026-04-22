class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = mutableListOf<Int>()
        for((i,j,k) in commands){
            val cut = array.copyOfRange(i-1, j)
            cut.sort()
            answer.add(cut[k-1])
        }
        return answer.toIntArray()
    }
}