def solution(n):
    return int(tri(n)[::-1], 3)

def tri(n):
    if n == 0:
        return '0'
    
    result = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        result = str(remainder) + result
    
    return result

# 간단하게
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

위 풀이에서 str(r) + result를 뒤집은 방식 이렇게
위는 정석으로 3진수를 나타내고 싶었음
