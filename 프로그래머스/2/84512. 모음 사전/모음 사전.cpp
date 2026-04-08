#include <string>
#include <bits/stdc++.h>

using namespace std;

string vowels = "AEIOU";
vector<string> dic;

// vowels에서 n개 뽑아서 순열 만들고, string으로 이어서, dic에 추가
void generate(string s, int depth){
    if(s.size() == depth){
        dic.push_back(s);
        return;
    }
    
    
    for(int i = 0; i < 5; i++){
        generate(s + vowels[i], depth);
    }
    
}

int solution(string word) {
    // 전역변수 초기화
    dic.clear();
    
    // 한자릿수부터 중복순열로 찾기
    for(int i = 1; i <=5; i++){
        generate("", i);  
    }
    
    // dic sort
    sort(dic.begin(), dic.end());
    
    // index 반환
    auto location = find(dic.begin(), dic.end(), word);
    
    return location - dic.begin() + 1;
}