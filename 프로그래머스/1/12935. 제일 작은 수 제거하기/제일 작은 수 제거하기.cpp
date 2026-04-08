#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr) {
    
    // 만약 리턴하려는 배열이 빈 배열이면 -1 채워서 리턴함 
    if(arr.size() == 1){
        return vector<int>(1, -1);
    }
    
    // 가장 작은 수를 제거하고 남은 배열을 리턴
    auto it = min_element(arr.begin(), arr.end());
    arr.erase(it);
    
    return arr;
}