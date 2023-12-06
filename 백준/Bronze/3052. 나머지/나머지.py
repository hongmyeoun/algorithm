N = 10

output = []

for _ in range(10):
    i = int(input()) % 42
    output.append(i)
    
print(len(set(output)))