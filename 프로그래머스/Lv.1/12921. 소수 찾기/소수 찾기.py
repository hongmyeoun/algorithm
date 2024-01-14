def solution(n):
    prime = set(i for i in range(2, n+1))
    
    for i in range(2, int(n**0.5)+1):
        if i in prime:
            prime -= set(j for j in range(i*2, n+1, i))
            
    return len(prime)

# 똑같은 에라스토테네스의 체 사용
def solution(n):
    num=set(range(2,n+1)) # 이런식으로 바로 생성 가능...

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

에라토스테네스의 체
0. 제곱근 이하의 배수들을 제거해나가 남는걸 세는 방식 -> 120까지면 11제곱인 121이 120보다 더 크므로 11미만의 배수들만 다 제거해주면 됨
1. 처음 나오는 수는 나두고
2. 처음 나오는 수의 배수는 싹다 제거
