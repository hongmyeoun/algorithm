def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]: # 비어있지 않으면 그냥 if문
            del cards1[0]
        elif cards2 and word == cards2[0]:
            del cards2[0]
        else:
            return "No"
    return "Yes"

# goal을 순회하면서
# 카드1의 첫단어와 비교해 같다면 카드1을 사용(삭제)
# 카드2의 첫단어와 비교해 같다면 카드2를 사용(삭제)
# 둘다아니면 "No"
# 끝났으면 "Yes"

# pop()을 사용
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
