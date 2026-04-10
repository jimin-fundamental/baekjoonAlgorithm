#include<bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> maps)
{
    int m = maps.size(); //세로
    int n = maps[0].size(); //가로
    
    queue<pair<int,int>> q; //BFS이니까 먼저 도착한 게 최단경로
    vector<vector<bool>> visited(m,vector<bool>(n, false));
    
    visited[0][0] = true;
    q.push({0,0});
    
    vector<int> dy = {-1, 1, 0, 0};
    vector<int> dx = {0, 0, -1, 1};
    
    // 가능한 길을 계속 나가기
    while(q.size() > 0){
       auto [y, x] = q.front();
        q.pop();
        
        //종료조건
        if ((y == m-1) && (x == n-1)){
            return maps[y][x];
        }
        
        for(int i = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            
            if((0 <= ny && ny < m  && 0 <= nx && nx < n) && (maps[ny][nx] == 1) && (!visited[ny][nx])){
                maps[ny][nx] = maps[y][x] + 1;
                visited[ny][nx] = true;
                q.push({ny,nx});
            }
        }
    }
    
    // 만약 q.size() == 0인데 도착하지 못했으면 
    return -1;
}