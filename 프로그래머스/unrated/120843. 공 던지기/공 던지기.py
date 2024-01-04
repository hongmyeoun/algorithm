def solution(numbers, k):
    count = 0
    numbers = numbers * k
    for i in range(0,len(numbers),2):
        count += 1
        if k == count:
            return numbers[i]

# 수학적 풀이...
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

k를 그냥 사용하면 k번째에 공을 받은 사람이 나옵니다. 
근데 문제에서 k번째에 던진 사람을 구하라 했음으로 k-1까지 입니다..

2 * (k - 1)는 0인덱스부터 공을 던지는 사람의 인덱스를 구함
% len(numbers)를 사용해 list 범위를 넘어가면 다시 돌아오게 함
