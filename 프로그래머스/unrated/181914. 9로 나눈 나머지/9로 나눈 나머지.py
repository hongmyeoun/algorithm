def solution(number):
    return eval('+'.join([digit for digit in number])) % 9