N, X = map(int, input().split())

while True:
    A = list(map(int, input().split()))
    if len(A) == N:
        break

output = []
for i in A:
    if i < X:
        output.append(i)

for i in output:
    print(i, sep=" ", end=" ")

