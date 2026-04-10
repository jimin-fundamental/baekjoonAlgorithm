#include <bits/stdc++.h>

using namespace std;

bool solution(vector<string> phone_book) {
    unordered_set<string> hash_map;
    for(string number: phone_book) hash_map.insert(number);
    
    // 내 접두사가 있나? 하고 찾는 거
    for(string number: phone_book){
        string prefix;
        for (int i = 0; i < number.size() - 1; i++){
            prefix += number[i];
            if(hash_map.count(prefix)) return false;
        }
    }
    return true;
}