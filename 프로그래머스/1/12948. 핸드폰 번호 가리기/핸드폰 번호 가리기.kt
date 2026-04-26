class Solution {
    fun solution(phone_number: String): String {
        var answer = ""
        var n = phone_number.length
        answer += "*".repeat(n-4)
        answer += phone_number.substring(n-4,n)
        
        return answer
    }
}