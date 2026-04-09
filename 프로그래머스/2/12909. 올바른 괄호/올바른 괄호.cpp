#include <bits/stdc++.h>

using namespace std;

bool solution(string s)
{
    // stack 만들기 //!!항상 뭐 정의할 때 타입(int, string, ...)도 같이 써줘야 돼
    stack<char> st;
    
    // ( 이면 넣고  
    // ) 이면 빼기
    for (char a: s){
        if (a == '('){
            st.push(a);
        }
        else{
            // 없는데 빼려고 하면 false return
            if(st.size()>0){
                st.pop();
            }
            else{
                return false;
            }
        }
    }
    // s 끝까지 보고 stack에도 남은 거 없으면 true return
    if(st.empty()){
        return true;
    } else{
        return false;
    }
}