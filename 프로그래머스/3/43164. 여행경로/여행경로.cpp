#include <bits/stdc++.h>

using namespace std;

vector<string> dfs(vector<vector<string>>& tickets, vector<string>& path, vector<bool>& visited, string cur, int tickets_size){
    path.push_back(cur);
    
    // 종료 조건
    if(path.size() == tickets_size + 1){
        return path;
    }
    
    for (int i = 0; i < tickets_size; i++){
        if (tickets[i][0] == cur && !visited[i]) {
            visited[i] = true;
            vector<string> result = dfs(tickets, path, visited, tickets[i][1], tickets_size);
            if(!result.empty()) return result;
            
            // 실패했다면 다시 복구하고 다음 i(다른 티켓)를 시도
            visited[i] = false; //백트래킹
        }
    }
    // 이 길로는 답이 안 나온다면 줬던 거 뺏고 돌아가기
    path.pop_back();
    
    // 실패 시 빈 벡터
    return {};
}


vector<string> solution(vector<vector<string>> tickets) {
    int len = tickets.size();
    vector<string> path;
    vector<bool> visited(len, false); //딱 맞춰서 초기화하기
    
    // 정렬해서 티켓 제공해서 사전순으로 정렬된 것부터 가도록 함. 
    sort(tickets.begin(), tickets.end());

    return dfs(tickets, path, visited, "ICN", len);
}