def solution(str1, str2):
    answer = ''
    for index in range(len(str1)):
        answer += str1[index] + str2[index]
    return answer