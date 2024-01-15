def solution(s):
    answer = 0
    check = s[0]
    count_x = 0
    count_else = 0
    splits = []

    idx = 0
    while idx < len(s):
        char = s[idx]
        if char == check:
            count_x += 1
        else:
            count_else += 1

        if count_x == count_else:
            splits.append(s[:idx+1])
            s = s[idx+1:]
            if s:
                check = s[0]
            count_x = 0
            count_else = 0
            idx = 0
        else:
            if idx == len(s)-1:
                splits.append(s)
                break
            idx += 1

    return len(splits)

# 글자를 순회하면서
# 그 글자를 세고, 아닌 글자를 센다
# 이때 그 수가 같다면, 그 인덱스까지 문자를 자름
# 반복