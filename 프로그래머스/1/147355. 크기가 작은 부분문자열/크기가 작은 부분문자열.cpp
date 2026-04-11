#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int n = p.size();
    // int np = stoi(p); << int는 10자리까지이므로 불가능
    long long np = stoll(p);
    
    for (int i = 0; i < t.size() - n + 1; i++){
        if(stoll(t.substr(i, n)) <= np) answer++;
    }
    
    return answer;
}