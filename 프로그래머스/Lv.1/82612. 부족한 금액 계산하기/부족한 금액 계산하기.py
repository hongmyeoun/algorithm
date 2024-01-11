def solution(price, money, count):
    pay = 0
    for i in range(1,count+1):
        pay += price * i

    return pay-money if pay-money > 0 else 0

# 등차수열
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
