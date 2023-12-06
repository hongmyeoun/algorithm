N = int(input())

while True:
    A = list(map(int, input().split()))
    if len(A) == N:
        break

print(min(A), max(A))
