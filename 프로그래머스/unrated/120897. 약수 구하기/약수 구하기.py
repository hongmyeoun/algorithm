solution = lambda n: sorted([i for i in range(1, n+1) if not n % i])

# 1부터 n까지 n을 나눴을때 나머지가 0이 되는 수를 append