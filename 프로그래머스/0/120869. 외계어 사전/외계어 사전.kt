class Solution {
    fun solution(spell: Array<String>, dic: Array<String>): Int {
        var answer: Int = 2
        for(word in dic){
            // map 만들기
            val check = mutableMapOf<String, Boolean>()
            for(s in spell){
                check[s] = false
            }
            
            for (i in word){
                check[i.toString()] = true
            }
            
            // 만약 check에 false가 남아있으면 continue 아니라면, return 1
            if(false in check.values){
                continue
            }
            else return 1
            
        }
        
        return answer
    }
}