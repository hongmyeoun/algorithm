def solution(my_string, n):
    return my_string[-n:]

# lamda
solution = lambda my_string, n: my_string[len(my_string)-n:]

# 람다식 설명
lambda arguments: expression

lambda: 람다 함수를 정의하는 키워드입니다.
arguments: 함수의 입력 매개변수들을 나타내는 부분입니다. 여러 개의 매개변수가 있을 경우 쉼표로 구분합니다.
expression: 함수의 반환값을 나타내는 표현식입니다.

ex) add = lambda x, y: x + y
add(2, 3) # 5
