class Solution {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        var answer = 0
        
        // 각 섬의 대표(parent)를 저장
        // 처음에는 자기 자신이 자기 그룹의 대표
        val parent = IntArray(n){it}
        
        // x가 속한 그룹의 대표 찾기
        fun find(x: Int):Int{
            if(parent[x] != x){
                parent[x] = find(parent[x])
            }
            return parent[x]
        }        
        
        // 두 섬을 연결
        // 이미 같은 그룹이면 false -> 더이상 연결 X
        // 다른 그룹이면 true -> 연결 가능
        fun union(a: Int, b:Int):Boolean{
            val pa = find(a)
            val pb = find(b)
            
            if(pa == pb) return false
            
            parent[pa] = pb
            
            return true
        }
        
        // 비용 낮은 간선부터 체크
        val sorted = costs.sortedBy{it[2]}

        
        var i = 0
        var edge = 0
        
        while(edge < n-1){
            val (x,y,cost) = sorted[i]
            
            // 두섬이 같은 그룹이 아니라면 연결
            if(union(x,y)){
                answer += cost
                edge++
            }
            
            i++
        }
        
        return answer
    }
}