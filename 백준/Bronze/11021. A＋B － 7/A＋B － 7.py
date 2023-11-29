T = int(input())
sumList = []
for _ in range(T):
    A, B = map(int, input().split())
    sumList.append(A + B)

for idx, i in enumerate(sumList):
    print(f"Case #{idx+1}: {i}")