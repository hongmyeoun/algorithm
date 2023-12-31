solution = lambda hp: (hp//5) + (hp%5)//3 + (hp%5)%3

# 의사코드
    장군개미 5
    병정개미 3
    일개미 1
    이거 완전 동전문제(그리디?)
    일단 가장 큰 수로 나눈다, 몫 을 result에 더함, 나머지가 있다면 나머지를 다음수로 나눔, 몫을 result에 더함

처음엔 동전문제처럼 ant_type list를 만들어 반복문으로 계산하려 했음
하지만 그러기엔 너무 낭비일 것 같아 품
연산 순서를 잘 알아두자...

연산순서
괄호 ()
지수 **
단항 연산자 - (음수), + (양수), ~ (비트 NOT)
곱셈 *, 나눗셈 /, 정수 나눗셈 //, 나머지 %
덧셈 +, 뺄셈 -
비트 시프트 <<, >>
비트 AND &
비트 XOR ^
비트 OR |
비교 연산자 ==, !=, <, >, <=, >=, in, not in, is, is not
논리 NOT not
논리 AND and
논리 OR or

몫과 나머지는 같은 순위이므로 내 식과 같이 괄호를 할 필요없고 앞에서부터 연산된다.

# ant_type을 사용하고 divmod()를 사용한 풀이
def solution(hp):
    answer = 0
    ant_type = [5, 3, 1]
    for ant in ant_type:
        d, hp = divmod(hp, ant)
        answer += d
    return answer

divmod(num1,num2) # num1을 num2 로 나눈 몫과 나머지를 출력하는 함수
여기선 몫을 answer로 쓰고, 나머지는 남은 hp
