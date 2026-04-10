#include <string>
#include <vector>

using namespace std;

void dfs(int n, vector<bool>& visited, vector<vector<int>>& computers, int cur){
    for (int i = 0; i < n; i++){
         if ((i != cur) && (computers[cur][i] == 1) && (!visited[i])){
             visited[i] = true;
             dfs(n, visited, computers, i);
         }
    }  
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);
    
    //인접리스트 만들기 -> 이미 computers로 주어짐
    
    //dfs로 돌면서 a점이랑 연결된 거 모두 돌기 
    //다 돌고 나서도 visited 하지 않은 곳 있으면 추가로 돌기
    for (int i=0; i < n; i++){
        if (!visited[i]) {
            visited[n] = true;
            dfs(n, visited, computers, i);
            answer++;
        }
    }
    return answer;
}