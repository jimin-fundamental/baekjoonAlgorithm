#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    // 리스트 길이 
    int n = genres.size();
    
    // 딕셔너리 (장르, (총 들은 횟수, [(i, plays[i]), ...]))
    map<string, pair<int, vector<pair<int, int>>>> dic;

    
    // 데이터 초기화
    for (int i = 0; i < n; i++){
        string genre = genres[i];
        int play = plays[i];
        
        dic[genre].first += play;
        dic[genre].second.push_back({play, i});
    }
    
    // first 기준으로 내림차순 정렬 -> custom 줘야겠지? 근데 map은 정렬이 안되므로
    vector<pair<int, string>> genre_count;
    for(auto a: dic){
        genre_count.push_back({a.second.first, a.first});
    }
    
    sort(genre_count.begin(), genre_count.end(), greater<pair<int, string>>());
    
    for(auto& [count, genre]: genre_count){
        vector<pair<int, int>> songs = dic[genre].second;
        
        sort(songs.begin(), songs.end(), [](auto a, auto b){
            if(a.first == b.first){
                return a.second < b.second;
            }
            return a.first > b.first;
        });
        
        answer.push_back(songs[0].second);
        if (songs.size() > 1) answer.push_back(songs[1].second);
    }
    
    return answer;
}