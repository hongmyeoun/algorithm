def solution(my_string):
    answer = [0] * 52
    for c in my_string:
        idx = ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26
        answer[idx] += 1
    return answer

ord() 는 해당 char의 아스키 코드값을 반환해줌
ord(c) - ord('A')로 총 52의 길이를 갖는 answer에서 해당 문자의 위치를 결정

# 다른사람 풀이
def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']
