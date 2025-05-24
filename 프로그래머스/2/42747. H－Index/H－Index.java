/*
h번 이상 인용된 논문이 h편 이상이고 
h의 최댓값이 이 과학자의 H-Index
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations
H-Index를 return
*/

/*
1. citations 정렬
2. 큰 수부터 돌면서 h index 만족하는지 테스트 */

import java.util.*;
import java.lang.Math;
import java.io.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations); //오름차순 정렬
        for(int i = citations[citations.length -1]; i >= 0 ; i--){ //큰 수부터 체크 
            int howMany = 0;
            for(int j = citations.length -1 ; j >= 0 ; j--){
                if(citations[j] >= i){
                    howMany += 1;
                    if(howMany >= i){
                        answer = i;
                        System.out.println("h-index는"+ answer);
                        return answer;
                    }
                    else{
                        continue;
                    }
                }
                else{
                    System.out.println(i+ "는 h-index가 안돼");
                    break;
                }
                
            }
        }
        return answer;
    }
}