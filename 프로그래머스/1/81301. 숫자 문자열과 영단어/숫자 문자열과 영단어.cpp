#include <bits/stdc++.h>

using namespace std;

int solution(string s) {
    vector<string> words = {"zero","one","two","three","four",
                      "five","six","seven","eight","nine"};
    
    for (int i = 0; i < words.size(); i++){
        int pos;
        while((pos = s.find(words[i])) != string::npos){
            s.replace(pos, words[i].size(), to_string(i));
        }
    }
    
    return stoi(s);
}