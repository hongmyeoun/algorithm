def solution(order):
    order = list(str(order))
    count = 0
    for i in order:
        if i == '3' or i == '6' or i == '9':
            count += 1
    return count

# count 사용
def solution(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
