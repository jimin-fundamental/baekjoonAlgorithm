#include <string>
#include <vector>

using namespace std;

int n; 
int answer = 0;

//nPn하면서 갱신 
void dfs_per(int depth, int rest_power, vector<vector<int>>& dungeons, vector<bool>& visited){
    // 끝까지 도달한 경우만 answer 갱신
    if(depth == n){
        return;
    }
    
    for(int i = 0; i < n; i++){
        if(!visited[i] && dungeons[i][0] <= rest_power){
            visited[i] = true;
            answer = max(depth+1, answer);
            dfs_per(depth+1, rest_power - dungeons[i][1], dungeons, visited);
            visited[i] = false; //백트래킹
        }
    }
    
}

int solution(int k, vector<vector<int>> dungeons) {
    n = dungeons.size();
    vector<bool> visited(n,false);
    
    dfs_per(0, k, dungeons, visited);
    
    return answer;
}