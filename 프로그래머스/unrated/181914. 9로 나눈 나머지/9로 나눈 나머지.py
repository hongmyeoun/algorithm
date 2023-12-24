def solution(number):
    return eval('+'.join([digit for digit in number])) % 9

# 다른사람 풀이라는데 문제와 맞는건가? 
# 문제에서 요구하는건 각자리 수를 합했을때 그걸 9로 나눴을때 나머지가 그 수를 9로 나눈 나머지랑 같다는걸 알려줬으니 각자리 합으로 푸는건줄...
def solution(number):
    return int(number) % 9
