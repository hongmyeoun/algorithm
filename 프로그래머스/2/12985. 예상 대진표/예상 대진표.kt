class Solution {
    fun solution(n: Int, a: Int, b: Int): Int {
        var answer = 0
        var _a = a
        var _b = b
        
        while (_a != _b) {
            ++answer
            _a = next_round(_a)
            _b = next_round(_b)
        }

        return answer
    }
    
    fun next_round(num: Int,): Int {
        return (num+1)/2
    }
}