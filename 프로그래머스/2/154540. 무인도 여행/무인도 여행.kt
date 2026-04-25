class Solution {
    fun solution(maps: Array<String>): IntArray {
        var answer = mutableListOf<Int>()
        
        // cy, cx, count
        val q = ArrayDeque<Pair<Int, Int>>()
        
        val visited = Array(maps.size) {BooleanArray(maps[0].length)}
        
        for(r in maps.indices){
            for (c in maps[0].indices){
                var count = 0
                
                if(maps[r][c] == 'X') continue
                
                
                // 연결되지 않은 거 추가
                if(!visited[r][c]){
                    visited[r][c] = true
                    q.addLast(Pair(r,c))
                }
                
                while(q.isNotEmpty()){
                   var (y,x) = q.removeFirst()
                   count += maps[y][x].digitToInt()
                   
                   // 연결된 거 다 넣기 
                   if (y+1 < maps.size){
                       if(!visited[y+1][x] && maps[y+1][x] != 'X'){
                           visited[y+1][x] = true
                           q.addLast(Pair(y+1, x))
                       }
                   }
                   if(y > 0){
                       if(!visited[y-1][x] && maps[y-1][x] != 'X' ){
                           visited[y-1][x] = true
                           q.addLast(Pair(y-1, x))
                       }
                   }
                   if( x+1 < maps[0].length){
                       if(!visited[y][x+1] && maps[y][x+1] != 'X' ){
                           visited[y][x+1] = true
                           q.addLast(Pair(y, x+1))
                       }
                   }
                   if( x > 0){
                       if(!visited[y][x-1] && maps[y][x-1] != 'X' ){
                           visited[y][x-1] = true
                           q.addLast(Pair(y, x-1))
                       }
                   }
                }
                
                // 큐가 끝났다는 건 하나의 덩어리 끝
                if(count > 0) answer.add(count)
            }
        }
        
        val sorted = answer.sorted().toIntArray()
        
        return if (answer.isEmpty()) intArrayOf(-1) else sorted
    }
}