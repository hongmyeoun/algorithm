solution = lambda q, r, code: ''.join([code[i] if i % q == r else '' for i in range(len(code))])
