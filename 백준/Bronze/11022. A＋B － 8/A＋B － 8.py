T = int(input())
sumList = []
for _ in range(T):
    A_B = list(map(int, input().split()))
    sumList.append(A_B)

for idx, i in enumerate(sumList):
    print(f"Case #{idx+1}: {i[0]} + {i[1]} = {sum(i)}")