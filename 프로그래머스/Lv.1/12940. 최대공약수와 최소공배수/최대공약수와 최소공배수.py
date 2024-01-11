import math

def solution(n, m):
    return [math.gcd(n,m), n*m//math.gcd(n,m)]

# 직접 풀이
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
