class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        val sorted1 = strings.sorted()
        val sorted2 = sorted1.sortedWith(
            compareBy<String> {it[n]}
        )
        
        return sorted2.toTypedArray()
    }
}