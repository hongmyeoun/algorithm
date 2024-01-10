from functools import reduce

def solution(a, b):
    return reduce(lambda x,y: x+y, list(range(min(a, b), max(a, b)+1)))

# 기본적인 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

# 시간복잡도 O(1)
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

S는 등차수열의 합,
n은 등차수열의 항의 개수,
a는 첫 번째 항,
l은 마지막 항

S = (n/2)*(a+l)

또는 총합 = 총갯수 * 평균
