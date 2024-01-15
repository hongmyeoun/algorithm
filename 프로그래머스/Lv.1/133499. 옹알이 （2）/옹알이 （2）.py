def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        if word in baby:
            answer += 1
        else:
            temp = ''
            check = ''
            for char in word:
                temp += char
                if temp != check and temp in baby:
                    check = temp
                    temp = ''
                    
            if temp == '':
                answer += 1
                    
    return answer

# babbling을 순회하면서
# 만약 baby랑 word가 같다면 바로 answer +1
# 그게 아니면 글자를 하나씩 체크를 함
# word의 한글자씩 temp에 넣어줌
# 이때 check변수를 만들고 check는 이전에 나온 발음인지 체크
# 만약 temp랑 check가 같지 않다면 temp가 baby에 있을때
# check에 temp를 넣어주어 중복체크를 한뒤 
# temp 초기화
# temp가 초기화 된체로 루프가 끝나면 -> 모든 문자 발음 가능
# answer +1

# .strip()으로 계산
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i: # 연속발음 배제
                i=i.replace(j,' ') # 나온 단어를 공백으로 치환
        if len(i.strip())==0: # 공백을 지웠을때 빈값이면 정답추가
            answer +=1
    return answer
