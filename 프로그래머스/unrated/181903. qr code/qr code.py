solution = lambda q, r, code: ''.join([code[i] if i % q == r else '' for i in range(len(code))])

# 처음 풀이
def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer

# 두번째
def solution(q, r, code):
    return ''.join([code[i] if i % q == r else '' for i in range(len(code))])

# 문제를 간단히 이해하기
결국 나머지로 나오는 숫자는 반복되고 그 간격은 나눈 수와 같다.
ex) 4로 나누면 나머지는 0, 1, 2, 3 -> 4개
solution = lambda q, r, code): code[r::q] # r인덱스 부터 q간격으로 슬라이싱
  
