solution = lambda message: len(message)*2

# 비트연산자
def solution(message):
    return len(message)<<1
  
<<: 비트 왼쪽 시프트 연산자
왼쪽으로 1만큼 비트를 이동

len(message) << 1은 문자열 message의 길이를 2배한 값을 나타냄
