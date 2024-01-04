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