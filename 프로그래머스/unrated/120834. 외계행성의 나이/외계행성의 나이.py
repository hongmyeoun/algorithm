def solution(age):
    alphabet = [chr(i) for i in list(range(ord('a'),ord('j')+1))]
    num = [str(i) for i in range(10)]
    PROGRAMMERS_962 = dict(zip(num, alphabet))
    
    return ''.join([PROGRAMMERS_962[i] for i in list(str(age))])