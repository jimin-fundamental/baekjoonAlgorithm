#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    // 0번 노드로부터 거리 저장
    vector<int> visited(n, -1);
    visited[0] = 0; //자기자신이므로 
    
    // 인접리스트 그래프 만들기
    vector<vector<int>> graph(n, vector<int>(0));
    
    for(vector<int> e: edge){
        //0번부터 시작하는 걸로 초기화
        int first = e[0]-1;
        int second = e[1]-1;
        
        graph[first].push_back(second);
        graph[second].push_back(first);
    }
    
    // 최단 경로 BFS
    queue<int> q;
    q.push(0); //0번 노드에서 시작
    
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        
        for(int x: graph[cur]){
            if(visited[x] == -1) {
                visited[x] = visited[cur] + 1;
                q.push(x);
            }
        }
    }
    
    for(int g: visited){
        cout<< g <<" ";
    }
    cout << endl;
    
    // 가장 멀리 떨어진 거리
    int far_amt = *max_element(visited.begin(), visited.end());
    
    // far_amt만큼 떨어진 노드 반환
    return count(visited.begin(), visited.end(), far_amt);
}