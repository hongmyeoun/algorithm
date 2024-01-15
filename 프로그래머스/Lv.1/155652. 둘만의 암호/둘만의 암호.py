def solution(s, skip, index):
    answer = ''
    alp = [chr(i) for i in range(ord('a'),ord('z')+1)]
    skip_alp = [c for c in skip]
    a = sorted(list(set(alp)-set(skip_alp)))*3
    for char in s:
        answer += a[a.index(char)+index]
    return answer

# 암호 규칙
# 1. s의 알파벳을 index만큼 뒤의 알파벳으로 바꿈(ord? 사용)
# 2. index만큼 뒤의 알파벳이 z를 넘어가면 다시 a로 돌아감(deque를 사용하거나 list를 두배로 만들기)
# 3. skip에 있는 알파벳은 제외하고 건너뜀

# deque를 리스트로 구현하기
# 만약 리스트의 길이를 넘어가면 처음부터 다시시작
# index%len(list)

# s의 문자와 skip의 문자는 겹칠 수 없다 -> 집합으로 풀이
# 알파벳에서 skip을 전부뺌, 이후 두배 -> 유사 deque
# 이러면 s의 문자를 알파벳 리스트에 대입해서 index를 더해주기만 하면 끝