#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    // 최댓값으로 초기화
    int answer = n;
    
    // 하나씩 wire 끊어서 인접리스트 만들어서 표현
    for(int no = 0 ; no < wires.size(); no++){
        
        // 1. 인접리스트 만들기
        vector<vector<int>> graph(n+1);
        
        for (vector<int> wire : wires){ //auto로 분해는 tuple, pair만 가능
            int a = wire[0];
            int b = wire[1];
            
            // 끊은 wire에 대해서는 그래프를 생성하지 않음
            if ( (a == wires[no][0] && b == wires[no][1])){
                continue;
            }
            graph[a].push_back(b); //이렇게 접근하려면 graph 초기화했어야 함 
            graph[b].push_back(a);
        }
        
        // 2. graph 돌면서 연결된 k 개의 노드 찾기
        queue<int> q;
        q.push(1);
        int k = 1;
        
        vector<bool> visited(n+1, false);
        visited[1]= true;
        
        while(q.size() > 0){
            int cur = q.front();
            q.pop();
            
            for(int node: graph[cur]){
                if(!visited[node]){
                    q.push(node);
                    visited[node] = true;
                    k++; //연결된 노드 하나 추가
                }
                
            }
        }
        // 3. 차이값이 최소이면 answer 갱신
        answer = min(abs(k - (n-k)), answer);
    }
    return answer;
}