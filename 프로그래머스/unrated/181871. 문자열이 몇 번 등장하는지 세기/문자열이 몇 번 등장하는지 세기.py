def solution(myString, pat):
    count = 0
    start_index = 0
    while True:
        index = myString.find(pat, start_index)
        
        if index == -1:
            break
        
        start_index = index + 1
        
        count += 1
        
    return count

# startswith(pat): 현재 부분 문자열이 주어진 패턴 pat으로 시작하는지 여부를 확인합니다.

def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
