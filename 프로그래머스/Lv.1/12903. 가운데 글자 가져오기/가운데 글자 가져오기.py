def solution(s):
    return s[len(s)//2] if len(s)%2 else s[len(s)//2-1:len(s)//2+1]

# else를 쓸 필요가 없음
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

홀수면 
5 -> 2:3 -> 2

짝수면
4 -> 1:3 -> 1,2
