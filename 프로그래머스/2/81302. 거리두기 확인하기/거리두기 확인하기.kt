import kotlin.math.*

class Solution {
    fun solution(places: Array<Array<String>>): IntArray {
        var answer = mutableListOf<Int>()
        
        // 각 참여자에 대해 true - 거리두기 잘 지킴. false -  거리두기 잘 지키지 X
        fun check(list:MutableList<Pair<Int, Int>>, place: Array<String>): Boolean{
            for(i in list.indices){
                for(j in i+1 until list.size){
                    val (y1, x1) = list[i]
                    val (y2, x2) = list[j]
                    
                    // 맨해튼 거리 체크
                    if((abs(y1-y2) +  abs(x1-x2)) <= 2){
                        // 가림막도 없어
                        if(y1==y2 || x1 == x2){
                            if(place[(y1+y2)/2][(x1+x2)/2] != 'X') {
                                return false
                            }
                        }
                        else{
                            if(place[y2][x1] != 'X' || place[y1][x2] != 'X') return false
                        }
                        
                    }
                }
            }
            
            return true
        }
        
        var p_list = mutableListOf<Pair<Int, Int>>()
        
        for(place in places){
            p_list.clear()
            
            for (r in 0 until 5){
                for (c in 0 until 5){
                    if(place[r][c] == 'P'){
                        p_list.add(Pair(r,c))
                    }
                }
            }
            
            if(check(p_list, place)) answer.add(1)
            else answer.add(0)
        }
        
        
        return answer.toIntArray()
    }
}