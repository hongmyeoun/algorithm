def solution(num_str):
    return sum([int(i) for i in num_str])

# map이용
solution=lambda num_str:sum(map(int, num_str))
map(int, num_str): 문자열로 된 각 숫자를 정수로 변환
