def solution(n):
    answer = []
    i = 2
    while i <= n:
        if not n % i:
            answer.append(i)
            n = n // i
            continue
        if n // i == 1 and n % i == 0:
            answer.append(i)
            break
        i += 1
    return sorted(list(set(answer)))

의사코드
    나눴을때 더이상 나눠지지 않을때 추가
    ex) n = 12
    12 / 2 = 6, 12 % 2 == 0 -> [2]
    6 / 2 = 3, 6 % 2 == 0 -> [2, 2]
    3 / 2, 3 % 2 == 1
    3 / 3 = 1, 3 % 3 == 0 => end [2, 2, 3]
    set([2,2,3])
    
    420 / 2 = 210 -> [2]
    210 / 2 = 105 -> [2,2]
    105 / 2, 105 % 2 == 1
    105 / 3 = 35 -> [2,2,3]
    35 / 3, 35 % 3 == 2
    35 / 4, 35 % 4 == 3
    35 / 5 = 7 -> [2,2,3,5]
    7 / 5, 7 % 5 == 2
    7 / 6, 7 % 6 == 1
    7 / 7 = 1, 7 % 7 == 0 => end [2,2,3,5,7]
    set([2,2,3,5,7])

if not n % i 조건에서 처음엔 continue를 사용 안했었다.
그랬더니 테스트는 다 통과 할 수 있었지만, 제출할때 테스트케이스들은 통과 못하는 경우가 생겼다.
그래서 문제에서 오름차순으로 정렬 하라 해서 sorted()를 추가 했는데도 문제가 있었고,
로직이 잘못 된 것을 확인.
의사코드처럼 나눴을때 그 나머지가 0이면 i로 계속 나눠야 하는데 그게 아니라 증가
continue로 해결, 사실 sorted()도 필요 없을 것 같다.(i가 2부터 커지기 때문)

# set을 안쓴 풀이
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

이렇게 하면 if d not in answer로 중복을 피할 수 있다.
오름차순 정렬은 d가 2부터 커지기 때문에 필요 없다.
