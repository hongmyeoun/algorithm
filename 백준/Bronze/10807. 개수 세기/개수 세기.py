N = int(input())

while True:
    A = input().split()
    if len(A) == N:
        break
    
find_A = input()

print(A.count(find_A))