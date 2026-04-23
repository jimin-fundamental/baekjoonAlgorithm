class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        // 네트워크 개수
        var answer = 0
        
        // 인접리스트로 computers가 주어짐
        
        val visited = BooleanArray(computers.size)
        
        val q = ArrayDeque<Int>()
        
        for(i in 0..computers.size-1){
            if(!visited[i]){
                q.addLast(i)
                visited[i] = true
                answer++
            }
            
            while(q.isNotEmpty()){
                val cur = q.removeFirst()

                for (computer in computers){
                    for(j in 0..computers[cur].size-1){
                        if(j != cur && !visited[j] && computers[cur][j] == 1){
                            q.addLast(j)
                            visited[j] = true
                        }
                    }
                }
            }
        }

        return answer
    }
}