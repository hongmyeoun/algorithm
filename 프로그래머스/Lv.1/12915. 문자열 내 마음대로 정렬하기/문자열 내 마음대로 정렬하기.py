def solution(strings, n):
    strings.sort(key=lambda s: s[n]+s)
    return strings

s[n] + s는
abca, bbca, cbca와 같은경우 n이 2일때
cabca, cbbca, ccbca로 본뒤 정렬을 하기 때문에 사전순으로 정렬가능
