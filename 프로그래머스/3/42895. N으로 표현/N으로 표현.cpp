#include <bits/stdc++.h>

using namespace std;

int solution(int N, int number) {
    // 1. vector 크기 할당 필수! (안 하면 Segfault)
    vector<set<int>> dp(9); //k개의 N으로 만들 수 있는 숫자들
    
    // 둘이 같으면 early return
    if(number == N){
        return 1;
    }
    
    // dp 최솟값 정의
    dp[1].insert(N);
    
    int n = 2; 
    
    //dp[n]를 계산해가다가 number 나오면 break하고 k 반환
    while(n <= 8){
        // 기본 숫자 붙인 거 넣기
        string num;
        for(int i = 0; i < n; i++){
            num += to_string(N);
        }
        dp[n].insert(stoi(num));
        
        //dp[k]와 dp[n-k]의 사칙연산
        for(int k = 1; k <= n-1; k++){
            
            // dp[k] 안에도 여러 값이 있는데 이 중 뭘 선택하냐
            for(int x: dp[k]){
                for(int y: dp[n-k]){
                    dp[n].insert(x+y);
                    dp[n].insert(x-y);
                    dp[n].insert(x*y);
                    if (y != 0) dp[n].insert(x/y);
                }   
            } 
        }
        
        if(dp[n].count(number)){
            return n;
        }
        
        n++; 
    }  
    return -1;
}