#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> targets) {
    
    // 사용한 미사일의 개수
    int used = 0;
    
    // targets 끝나는 점 기준 정렬
    sort(targets.begin(), targets.end(), [](vector<int> a, vector<int> b){
        return a[1] < b[1];
    });
        
    // 마지막으로 쏜 요격 미사일 위치(실수 좌표)
    // 처음 좌표는 작은 값으로 초기화
    double last_shot = -1.0;

   for(int i = 0; i < targets.size(); i++){
        int start = targets[i][0];
        int end = targets[i][1];
        
       // 만약 새로운 미사일이 '마지막으로 쏜 위치'보다 뒤에 있다면, 기존 미사일로는 못 맞춤
       if(start >= last_shot){
           // 새로 한 발을 쏨
           // 위치: 이 미사일이 끝나기 직전에!
           // 끝나기 직전 쏘는 거를 이런 식으로 표현한다고 우리끼리 정하기
           last_shot = end;
           used++;
       }
   }
    return used;
}