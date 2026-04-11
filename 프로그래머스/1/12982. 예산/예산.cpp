#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    // 오름차순으로 정렬
    sort(d.begin(), d.end());
    
    // int k = 1 부터 시작해서 1씩 올리면서 작은 거부터 더해보기. budget 넘으면 그 전 값 return하고 종료 
    for(int k = 1; k < d.size()+1; k++){ //몇 개의 부서?
        int count = 0;
        for(int i = 0; i < k; i++){
            count += d[i];
        }
        if(count > budget) return k-1;
    }
    
    return d.size();
}