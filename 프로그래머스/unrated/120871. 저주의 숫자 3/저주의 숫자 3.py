def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while not answer%3 or '3' in str(answer):
            answer += 1
    return answer

# 처음 풀이
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
    # curse_numlist = []
    # # curse_numlist의 index가 n과 같아지면 종료
    for i in range(1000):
        if not i%3 or '3' in str(i):
            continue
        curse_numlist.append(i)
    return curse_numlist[n-1]

큰 수는 표현 불가, 리스트 형태 저장으로 메모리 낭비, 딱 필요한 만큼만 계산하는게 아니라서 속도 비효율

이전에 range(100)으로 했는데, 이게 n의 값이 100까지지, curse_numlist의 길이가 100까지 안됐기 때문에 run time error가 떴던거 같음
하지만 range(1000)으로 바꾸고 그냥 돌려봤는데 제출이 됨

입력된 값만큼만 계산하도록 식을 수정하고 싶었음
그러려면 n만큼 순회하고, while안에서 값이 증가하는 식을 만들어야 됐음
그래서 range(n)만큼 순회를 하면서 값을 1씩 증가시키면서, 조건이 맞게되면 그 값을 스킵하는 방식으로 1을 더하는 방식을 채용
