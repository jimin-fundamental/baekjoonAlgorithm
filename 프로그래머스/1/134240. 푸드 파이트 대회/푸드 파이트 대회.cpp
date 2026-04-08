#include <bits/stdc++.h>

using namespace std;

string solution(vector<int> food) {
    string list = "";
    
    for(int idx= 1; idx < food.size(); idx++){
        int amount = food[idx];
        int num = amount / 2;
        
        for(int i = 0; i < num; i++){
            list += to_string(idx);
        }
    }
    string rlist(list.rbegin(), list.rend());
    list = list + "0" + rlist;
    
    return list;
}