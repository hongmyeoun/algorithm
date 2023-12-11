def solution(str1, str2):
    answer = ''
    for index in range(len(str1)):
        answer += str1[index] + str2[index]
    return answer

# join을 활용한 코드(다른풀이)
def solution(str1, str2):
    answer = ''.join([str1[index] + str2[index] for index in range(len(str1))])
    return answer
