class Solution {
    fun solution(array: IntArray): Int {
        // 중앙값 인덱스 
        var idx = (array.size -1) / 2
        
        // 정렬
        array.sort()
        
        return array[idx]
    }
}