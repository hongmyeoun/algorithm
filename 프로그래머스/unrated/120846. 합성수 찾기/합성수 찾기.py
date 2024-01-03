def solution(n):
    count = 0
    for i in range(1,n+1):
        if is_composite(i):
            count += 1
    return count

def is_composite(n):
    return int(len([i for i in range(1,n+1) if not n%i]) >= 3)

# 아주 좋은 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

필요한 수만 찾음
반복 범위를 줄이기 위해, 대부분 자연수의 약수는 대상의 제곱근 이하의 약수 하나와 이상의 약수 하나씩 한 쌍을 이룬다는 점을 응용해 i의 제곱근까지 반복하게 한 다음, 
4나 9등의 제곱수를 고려해 +1을 해서 예외를 해결한 경우입니다!
가운데 약수를 기준으로 대칭적인 형태이기 때문에, 제곱근까지만 (가운데 약수까지만) 확인하면 됩니다.
