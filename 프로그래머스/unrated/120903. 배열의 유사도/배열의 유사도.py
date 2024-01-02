def solution(s1, s2):
    count = 0
    for i in s2:
        for j in s1:
            if j == i:
                count += 1
    return count