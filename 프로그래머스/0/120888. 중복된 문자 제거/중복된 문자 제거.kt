class Solution {
    fun solution(my_string: String): String {
        var answer: String = ""
        //딕셔너리
        val dic = mutableMapOf<Char, Int>()
        
        
        for(m in my_string){
            if(m in dic){
                continue
            }
            else{
                dic[m] = 1
                answer += m.toString()
            }
        }
        
        return answer
    }
}