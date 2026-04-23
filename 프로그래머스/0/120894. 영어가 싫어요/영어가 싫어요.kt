class Solution {
    fun solution(numbers: String): Long {
        var answer = ""
        val arr = arrayOf("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        
        var idx1 = 0
        var idx2 = 1
        
        while(idx2 < numbers.length){
            // idx1 ~ idx2의 string 뽑아내기
            var string = ""
            for(idx in idx1..idx2){
                string += numbers[idx]
            }
            
            if(string in arr){
                var idx = arr.indexOf(string)
                answer += idx.toString()
                idx1 = idx2 + 1
                idx2 = idx1 + 1
            }
            else{
                idx2++
            }           
        }
        return answer.toLong()
    }
}