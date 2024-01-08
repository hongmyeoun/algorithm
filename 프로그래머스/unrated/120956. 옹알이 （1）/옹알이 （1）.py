def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        for j in baby:
            babbling[i] = babbling[i].replace(j,'1')
        if all(c=='1' for c in babbling[i]):
            answer += 1
            
    return answer
# babbling의 단어에서 baby에 포함된 단어를 1로 replace 시도했을때
# 1이면 count