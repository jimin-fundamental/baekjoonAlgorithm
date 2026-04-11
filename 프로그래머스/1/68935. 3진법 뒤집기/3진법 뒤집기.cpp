#include <bits/stdc++.h>

using namespace std;


// 3진법 후 앞뒤 반전해서 return
string three(int n){
    string answer;
    
    while(n >= 3){
        int rest = n % 3;
        answer += to_string(rest);
        n = n / 3;
    }
    answer += to_string(n);
    
    return answer;
}

int solution(int n) {
    int answer = 0;
    string k = three(n);
    int len = k.size();
    
    int multi = 1;
    for (int i = 0; i < len; i++){
        // 뒷자리부터 ㄱㄱ idx = len - i -1 
        int idx = len - i  -1;
        
        answer += (k[idx] - '0')*multi;
        multi *= 3;
    }
    
    return answer;
}