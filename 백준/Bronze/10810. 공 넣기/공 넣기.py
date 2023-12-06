N, M = map(int, input().split())

# 크기가 N인 0으로 채워진 리스트생성
basket = [0] * N

for _ in range(M):
    # i부터 j까지 k로 채움
    i, j, k = map(int, input().split())
    basket[i-1:j] = [k] * (j-(i-1))

for ball in basket:
    print(ball, end=" ")