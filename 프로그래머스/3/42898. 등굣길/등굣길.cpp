#include <bits/stdc++.h>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    // dp[(2,2)] = (2,2)까지 갈 수 있는 최단경로의 개수
    // 기존 (1,1)으로 좌표계 통일
    // puddles 안에 있는 곳은 dp[i] = 0, 좌표 밖의 구간을 사용해서 계산해야 할 경우 걍 0으로 계산하기
    vector<vector<long long>> dp(n+1, vector<long long>(m+1, 0));
    dp[1][1] = 1;
    
    for(int y = 1; y < n+1; y++){
        for(int x = 1; x < m+1; x++){
            // {1,1}은 패스
            if(y==1 && x==1) continue;
            
            // puddles면 0으로 취급
            vector<int> yx = {x,y}; //이렇게 정의해서 해야돼?? 바로 넣으면 안돼? <- puddle 데이터 대칭 아닌 거 테케 넣어보기
            if(count(puddles.begin(), puddles.end(), yx)) continue;
            
            //dp[(y,x)] = dp[(y-1, x)] + dp[(y, x-1)] // 만약 없으면 0으로 취급
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1000000007;
        }
    }
    return (int)dp[n][m];
}