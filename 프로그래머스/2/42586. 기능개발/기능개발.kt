class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        val done = BooleanArray(progresses.size) //false로 초기화됨
        
        
        // 모든 작업이 끝날 때까지 
        while(!done[progresses.size -1]){
            // 하루의 작업 
            var count = 0
            for(i in 0 until progresses.size){
                if(!done[i]){
                    // 작업률 진행 
                    progresses[i] += speeds[i]

                    // 100 넘으면 배포 & 앞의꺼도 배포됐으면 
                    if((i == 0 || done[i-1]) && progresses[i] >= 100){
                        count++
                        done[i] = true
                    }
                }  
            }
            if(count > 0) answer.add(count)
        }
        
        return answer.toIntArray()
    }
}