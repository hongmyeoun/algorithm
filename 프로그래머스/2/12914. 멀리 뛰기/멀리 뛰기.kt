class Solution {
    fun solution(n: Int): Long {
        var answer: Long = 0
        
        if (n == 1) {
            return 1%1234567
        } else if (n == 2) {
            return 2%1234567
        }
        
        var pre = 1L
        var next = 2L
        var temp = 0L
        
        for (i in 1..n-2) {
            temp = pre
            pre = next
            next = (temp + next)%1234567
        }
        
        answer = next
        return answer
    }
}