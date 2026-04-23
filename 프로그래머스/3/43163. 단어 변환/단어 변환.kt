class Solution {
    
    fun one_different(a:String, b: String): Boolean{
        var count = 0
        for(i in 0 until a.length){
            if(a[i] != b[i]) count++
        }
        return (count == 1)
    }
    
    fun solution(begin: String, target: String, words: Array<String>): Int {
    
        val visited = BooleanArray(words.size)
        
        if (target !in words) return 0
        
        val q = ArrayDeque<Pair<String, Int>>()
        q.addLast(Pair(begin, 0))
        
        while(q.isNotEmpty()){
            val (cur, count) = q.removeFirst()
            
            if(cur == target) return count
            
            for(i in 0 until words.size){
                val word = words[i]
                if(one_different(word, cur) && !visited[i]){ // 근데 이렇게 하면 visited를 거를 수 있나? 여러개의 옵션 중에 하나만 선택하는 거 아닌가?
                    q.addLast(Pair(word, count + 1))
                    visited[i] = true
                }
            }
        }
        return 0
    }
}