def solution(s):
    answer = []
    check = []
    for c in range(len(s)):
        if s[c] not in check:
            answer.append(-1)
            check.append(s[c])
        else:
            answer.append(c-(len(check) - check[::-1].index(s[c]) - 1))
            check.append(s[c])
    return answer

# 그 글자가 언제 어디서 나왔는지 저장을 해야함
# 저장된게 없다면 -1, 있다면 그 위치와 현재 위치를 빼줌
# 어떻게함?
# 일단 check 리스트를 만들어서 값을 저장
# 저장하기 전에 값이 있는지 확인을하고 추가해줌
# 값이 없다면 -1을 답에 추가해주고, check에 값을 추가
# check에 중복요소가 있다면
# check에 뒤에서부터 중복요소의 index를 가져와 현재 index에서 뺀값을 답에 추가
# check에 현재값을 추가
