def solution(num_list):
    answer = 0
    for i in num_list:
        temp = i
        while temp != 1:
            if temp % 2: # 홀수이면
                temp = (temp-1)//2
                answer += 1
            else:
                temp //= 2
                answer += 1
    return answer

# bin로 풀이
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

len(bin(i)) - 3을 통해 '0b'의 길이 2와 마지막 비트(1)의 길이 1을 뺍니다. 
이는 정수 i를 1로 만드는데 필요한 연산 횟수와 일치합니다. 
예를 들어, 10은 이진수로 1010이고, 3번의 연산이 필요합니다 (첫 번째 '1'은 무시됩니다).
