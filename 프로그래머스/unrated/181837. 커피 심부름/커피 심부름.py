def solution(order):
    answer = 0
    americano = ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    cafelatte = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte"]
    for menu in order:
        if menu in americano:
            answer += 4500
        elif menu in cafelatte:
            answer += 5000
    return answer

# 라떼로 판별하기
def solution(order):
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += 500
        answer += 4500

    return answer
