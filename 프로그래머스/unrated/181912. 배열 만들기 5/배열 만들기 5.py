def solution(intStrs, k, s, l):
    return [int(i[s:s + l]) for i in intStrs if int(i[s:s+l]) > k]

# 람다식으로 풀기
def solution(intStrs, k, s, l):
    return list(filter(lambda x: x > k, map(lambda x: int(x[s:s + l]), intStrs)))
