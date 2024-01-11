def solution(s):
    answer = ''
    s = s.split(' ')
    for idx, i in enumerate(s):
        for c in range(len(i)):
            if not c%2:
                answer += i[c].upper()
            else:
                answer += i[c].lower()
        if idx < len(s)-1:
            answer += ' '
    return answer