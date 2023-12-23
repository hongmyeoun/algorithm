def solution(a, b, c):
    if a == b and b == c and c == a:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    # |은 비트연산자, or을 써야됨
    elif a == b or b == c or c == a:
        answer = (a+b+c)*(a**2+b**2+c**2)
    # elif a != b and b != c and c != a:
    else:
        answer = a+b+c
        
    return answer