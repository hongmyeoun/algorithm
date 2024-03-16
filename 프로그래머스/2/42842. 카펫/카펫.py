def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            width = yellow / i
            height = i
            if brown == (height + width + 2) * 2:
                return width + 2, height + 2
            
# 다시 생각해 보니
# 가로 세로의 길이는
# yellow의 약수(가운데 값 두개)중 큰 값 + 2가 가로
# 작은 값 + 2가 세로 임

# 약수 쌍 찾는 문제
# 1부터 yellow의 제곱근까지 약수를 찾아내면 됨
# 이때 약수가 다 되는건 아니니깐 가운데 두 값을 찾으려면 brown 값을 이용
# brown = (약수쌍중 작은값 * 2) + (약수쌍중 큰값 + 2) * 2
# brown = (약작값 + 약큰값 + 2) * 2

# 이 조건이 맞다면 약수쌍 + 2를 반환

# y가 소수가 아니면 
# 약수의 중간수 중 큰 수 = 가로의 길이
# 중간수 중 작은수 = 세로의 길이

# 소수면?
# 자기 자신이 가로
# 세로는 3

# 이때 갈색 격자의 수와 노란 격자의 순에 제한이 있음
# y를 통해 b 유추

# 소수가 아닐때
# b는 
# (가로의 길이 + 2) * 2 (맨위, 맨아래)
# (세로의 길이 - 2) * 2 (양옆)를 더해
# b = (가 + 2) * (세 - 2) * 2

# 소수일때
# (y + 2) * 2 (맨위, 맨아래)
# + 2 (양옆)
# b = (y + 2) * 2 + 2

# y = 1, b = 8
# b 3
# b 2, y 1
# b 3
# [3,3]

# y = 2, b = 10
# b 4
# b 2, y 2
# b 4
# [4,3]

# y = 3, b = 12
# b 5
# b 2, y 3
# b 5
# [5,3]

# y = 4, b = 12
# b 4
# b 2, y 2
# b 2, y 2
# b 4
# [4,4]

# y = 5, b = 16
# b 7
# b 2, y 5
# b 7
# [7, 3]

# y = 6, b = 14
# b 5
# b 2, y 3
# b 2, y 3
# b 5
# [5, 4]

# y = 7, b = 20
# b 9
# b 2, y 7
# b 9
# [9, 3]

# y = 8, b = 14
# b 6
# b 2, y 4
# b 2, y 4
# b 6
# [6, 4]

# y = 9, b = 16
# b 5
# b 2, y 3
# b 2, y 3
# b 2, y 3
# b 5
# [5, 5]

# y = 10, b = 16
# b 7
# b 2, y 5
# b 2, y 5
# b 7
# [7, 4]

이분 탐색을 이용한 풀이
# x * y = brown + yellow
# x + y = (brown + 4)//2

# x + y 에서 x, y를 정한다. 이때 x와 y의 차가 작을 수록 그 곱은 더 커진다.
# 이를 이용해서 이분 탐색으로 그 차의 크기를 조절해서 답을 구한다.

# x <= y 라고 하면, x는 1 ~ (x+y)//2 의 값을 가진다.
def solution(brown, yellow):
    m = brown + yellow
    s = (brown + 4) // 2

    # x가 가질 수 있는 최대값
    diff = (s // 2)

    # x가 가질 수 있는 최대값의 절반
    x = diff // 2
    y = s - x
    diff //= 2

    while x * y != m:
        if diff != 1:
            diff //= 2

        if x * y > m:
            x -= diff
            y += diff

        else:
            x += diff
            y -= diff

    return [y, x]

출처 : https://school.programmers.co.kr/questions/52491
고정값 x + y를 이용해 x*y의 순서쌍을 찾는 방식
이렇게 풀게 되면 brown을 이용하게 되므로(s) 시간복잡도가 O(log brown)이 된다.
기존 yellow를 이용했을땐 O(sqrt(yellow))였던 거보다 더 효율적이게 된다.

# 둘레의 길이를 이용
가로 * 세로 = 격자 합, 둘레의 합(가로*2 + 세로*2 - 겹치는부분4) = 갈색 둘레
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
