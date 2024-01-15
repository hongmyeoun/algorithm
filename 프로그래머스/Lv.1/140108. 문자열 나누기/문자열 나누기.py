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

# 같을때 바로 answer를 더하면서 리스트 생성 X
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
결과를 낼때 마지막 분리값을 안더해도 되는가?
s="abracadabra"인 경우 ab - ra - ca - da - br - a
i='a' -> answer = 1 sav1 = 1, sav2 = 0
i='b' -> sav2 = 1
i='r' -> answer = 2 sav1 = 2, sav2 = 1 a='r'
i='a' -> sav2 = 2
i='c' -> answer = 3 sav1 = 3, sav2 = 2, a='c'
i='a' -> sav2 = 3
i='d' -> answer = 4 sav1 = 4, sav2 = 3, a='d'
i='a' -> sav2 = 4
i='b' -> answer = 5 sav1 = 5, sav2 = 4, a='b'
i='r' -> sav2 = 5
i='a' -> answer = 6 sav1 = 6, sav2 = 5, a='a'
됨
