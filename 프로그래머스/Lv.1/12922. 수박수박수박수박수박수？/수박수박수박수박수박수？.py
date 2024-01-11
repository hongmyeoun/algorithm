def solution(n):
    answer = ''
    for i in range(n):
        if i%2:
            answer += '박'
        else:
            answer += '수'
    return answer

# 슬라이싱
def water_melon(n):
    str = "수박"*n
    return str[:n]

solution 함수:
각 반복에서 문자열에 문자를 추가하므로, 반복이 진행됨에 따라 메모리에 새로운 문자열이 계속 생성됩니다.
이는 n이 커질수록 메모리 사용량이 증가할 수 있습니다.
    
water_melon 함수:
"수박"을 미리 만들어 놓고, 슬라이싱을 통해 필요한 부분만 반환하므로, 추가적인 메모리 사용이 거의 없습니다.
메모리 사용 측면에서는 상대적으로 효율적입니다.
