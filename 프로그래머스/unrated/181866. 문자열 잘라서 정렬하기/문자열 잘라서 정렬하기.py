def solution(myString):
    return sorted([i for i in myString.split('x') if i != ''])

# split을 두번사용
def solution(myString):
    answer = ' '.join(myString.split('x')).split()
    return sorted(answer)
