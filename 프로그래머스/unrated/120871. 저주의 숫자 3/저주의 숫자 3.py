def solution(n):
    # 3x마을이 사용하는 숫자는 3의 배수와 숫자 3을 안씀
    # 3의 배수를 안씀
    # 3을 안씀
    # 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    # 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29, 40, 41
    # 3의 배수 : n을 3으로 나눴을때 나머지가 0인 수 // not n % 3
    # 3인 수 : 글자 안에 3이 들어간 수 // '3' in str(n)
    # 1부터 100까지 저주마을 숫자를 저장한 list를 생성 -> 입력조건이 그거임
    # n값을 저주마을 숫자리스트 index로 찾아냄
    curse_numlist = []
    # curse_numlist의 index가 n과 같아지면 종료
    for i in range(1000):
        if not i%3 or '3' in str(i):
            continue
        curse_numlist.append(i)
    return curse_numlist[n-1]