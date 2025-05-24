/*
종류별로 최대 1가지
한개이상의 의상
코니가 가진 의상들이 담긴 2차원 배열 clothes
서로 다른 옷의 조합의 수를 return 
*/

/*
1. 종류별로 몇개인지 DICTIONARY로 저장
2. (각 종류 +1) 다 곱하고 -1*/

import java.util.*;
import java.lang.Math;
import java.io.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> types = new HashMap<>();
        for(String[] cloth: clothes){
            if (types.containsKey(cloth[1])){
                types.put(cloth[1],types.get(cloth[1]) +1);
            }
            else{
                 types.put(cloth[1],1);
            }
            
        }
        for(String type: types.keySet()){
            answer *= (types.get(type)+1);
        }
        return (answer-1);
    }
}