/*- 일주일동안
- 출근희망시각+10분까지 출근
- 토욜(6), 일욜(7)은 상관 X
- 매일 한번씩 출근
- 시각 = 시*100+분
- 상품받을직원의 수 return
- 직원 n명이 설정한 출근 희망 시각을 담은 1차원 정수 배열 schedules
직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열 timelogs
이벤트를 시작한 요일을 의미하는 정수 startday
*/
/*
1. 1번 사람부터 돌면서 timelogs 1번째 배열부터 체크(사람마다 startdaay)
2. 중간에 늦으면 & 주말이 아니면 break
3. 끝까지 다 돌면 return
*/


class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        for(int j = 0; j < timelogs.length;j++){
            boolean late = false;
            int duetime = ((schedules[j]%100+10)/60 + schedules[j]/100)*100 + (schedules[j]%100+10)%60;

            
            for(int i=0; i <7; i++){
                
                if(timelogs[j][i] > (duetime) && ((0< ((startday+i)%7)) && (((startday+i)%7)) <=5)){
                    late = true;
                    System.out.println(j+"가"+i+"번째 날에"+((startday+i)%7)+"번째 요일에 지각함");
                    break;
                }
                
            }
            if(!late){
                    answer++;
                }
        }
        return answer;
    }
}