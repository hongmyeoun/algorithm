class Solution {
    fun solution(n: Int): Long {
        var answer: Long = 0
        
        if (n == 1) {
            return 1%1234567
        } else if (n == 2) {
            return 2%1234567
        }
        
        var pre = 1L // 파이썬과 다르게 타입 명시를 해야한다...
        var next = 2L
        var temp = 0L
        
        for (i in 1..n-2) {
            temp = pre
            pre = next
            next = (temp + next)%1234567 // next에서 값을 계산 안해서 한참 헤맸다...
        }
        
        answer = next
        return answer
    }
}

// when을 사용한 결과값 반환...
class Solution {
    fun solution(n: Int): Long {
        var first: Long = 1
        var second: Long = 2
    return when(n) {
        1 -> first
        2 -> second
        else -> {
            var current: Long = first + second
            for (num in 3..n) {
                current = (first + second) % 1234567
                first = second
                second = current
            }
            current
        }
    }
    }
}
