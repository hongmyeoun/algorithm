T = int(input())

output = []
for _ in range(T):
    C = input()
    result = C[0] + C[-1]
    output.append(result)

for i in output:
    print(i)