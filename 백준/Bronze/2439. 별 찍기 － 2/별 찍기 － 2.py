T = int(input())

for i in range(1, T + 1):
    space = T - i
    print(" " * space + "*" * i, sep="\n")