class Solution {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        val answer = mutableListOf<String>()
        
        // 정렬
        val sorted = tickets.sortedWith(
            compareBy<Array<String>> {it[0]}.thenBy{it[1]}
        )
        
        val route = mutableListOf("ICN")
        val visited = BooleanArray(tickets.size)
        
        fun dfs(route: MutableList<String>):MutableList<String>{
            if(route.size == sorted.size +1){
                for(r in route){
                    answer.add(r)
                }
                return answer //여기에서 반환을 하는데 왜 answer에 계속 덧붙여지는 거지???
            }
            
            val cur = route[route.size -1]
            
            //다음 경로 탐색
            for(i in sorted.indices){
                if(sorted[i][0] == cur && !visited[i]){
                    route.add(sorted[i][1])
                    visited[i] = true
                    
                    if (dfs(route).size == sorted.size +1){ //여기서도 반환을 해줘야되는구나!!
                        return answer
                    }
                    
                    // 그 경로가 맞지 않았다면
                    route.removeAt(route.size -1)
                    visited[i] = false
                }
            }
            
            return answer
        }
        
        return dfs(route).toTypedArray()
    }
}