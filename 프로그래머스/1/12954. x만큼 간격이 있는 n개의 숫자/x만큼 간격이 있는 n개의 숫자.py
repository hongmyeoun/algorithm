def solution(x, n):
    return [i*x for i in range(1,n+1)]

# 런타임 에러가 난 식
    # return list(range(x,(n+1)*x,x))
    # 이유는 뭔가 값이 n이 1000이랑 x가 최대값 근처로 가서
    # 라고 생각했지만 step 부분에 x값이 0이되면 오류가 난다.
