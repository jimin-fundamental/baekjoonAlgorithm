class Solution {
    
    val answer = mutableListOf<Array<String>>()
    
    fun dfs(
        route: MutableList<String>, 
        tickets: List<Array<String>>, 
        visited: BooleanArray
    ){
        // 종료조건
        if(route.size - 1 == tickets.size){
            answer.add(route.toTypedArray()) //StringArray로 바꾸려면 toTypedArray()
            return
        }
        
        // 종료되지 않았다면, 현재 cur와 연결된 다른 루트들 모두 추가
        var cur = route[route.size - 1]
        
        for(i in tickets.indices){
            if(tickets[i][0] == cur && !visited[i]){
                route.add(tickets[i][1])
                visited[i] = true
                
                dfs(route, tickets, visited) //여기서 return하면 뒤의 코드 실행 X
                
                visited[i] = false //백트래킹
                route.removeAt(route.size - 1) // 백트래킹할 거면 route에서도 지워야 돼
            }
        }
    }
    
    fun solution(tickets: Array<Array<String>>): Array<String> {
        val visited = BooleanArray(tickets.size)
        
        val sorted = tickets.sortedWith(
            compareBy<Array<String>> {it[0]}.thenBy{it[1]}
        )
        
        val route = mutableListOf("ICN")

        dfs(route, sorted, visited)
        
        return answer[0]
    }
}