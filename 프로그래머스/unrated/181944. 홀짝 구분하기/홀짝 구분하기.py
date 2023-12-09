n = int(input())

if 1 <= n <= 1000:
    if n % 2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')