#include <bits/stdc++.h>

using namespace std;

bool one_diff(string a, string b){
    int n = a.size();
    int count = 0;
    for(int i = 0; i < n; i++){
        if(a[i] != b[i]) count++; //이거 언제 + 되더라?
        if(count > 1) return false;
    }
    return true;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    queue<pair<string, int>> q;
    vector<bool> visited(words.size(), false);
    
    // early return
    if(! count(words.begin(), words.end(), target)) return 0;
    
    // 로직 시작
    // q.push({begin, 0}); //이렇게 하면 자동으로 pair로 인식되나? vector일 수도 있고 tuple일 수도 있는데? <- 위에서 큐 정의할 때 해줘서 ㄱㅊ
    q.push({begin, 0});
    
    while(!q.empty()){
        auto a = q.front();
        string cur = a.first;
        int count = a.second;
        q.pop();
        
        for(int i = 0; i < words.size(); i++){
            string next = words[i];
            if(one_diff(cur, next) && !visited[i]){
                if(next == target) return count +1;
                q.push({next, count + 1});
            }
        }
    }
    
    return answer;
}