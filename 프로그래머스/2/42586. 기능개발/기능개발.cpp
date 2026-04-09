#include <string>
#include <vector>

using namespace std;


vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    //모든 작업이 끝날 때까지 반복
    int count = 0;
    int idx = 0;
    while(idx < progresses.size()){
            if(progresses[idx] >= 100){
                count++;
                idx++;
            }
            else{
                if(count != 0){
                    answer.push_back(count);
                    count = 0; //초기화
                }
                 // 하루가 지날 때마다 모든 progresses에 speeds 더하기
                for(int k = 0; k < progresses.size(); k++){
                    progresses[k] += speeds[k];
                }
            }
        }
    
    //남아있는 값 정리
    if(count != 0) answer.push_back(count);
    
    return answer;
}