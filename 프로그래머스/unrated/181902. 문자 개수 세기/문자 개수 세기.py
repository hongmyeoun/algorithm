def solution(my_string):
    answer = [0] * 52
    for c in my_string:
        idx = ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26
        answer[idx] += 1
    return answer