class Solution {
    fun solution(arr: IntArray): Int {
        var answer = arr[0]
        for (num in arr) {
            answer = num * answer / gcd(num, answer)
        }
        return answer
    }
    
    fun gcd(a: Int, b: Int): Int{
        return if (b==0) a else gcd(b, a % b)
    }
}