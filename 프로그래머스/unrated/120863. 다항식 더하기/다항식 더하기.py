def solution(polynomial):
    x = []
    c = []
    for i in polynomial.split():
        if 'x' in i:
            x.append(i)
        elif i != '+':
            c.append(int(i))
            
    for i in range(len(x)):
        if x[i] == 'x':
            x[i] = 1
        else:
            x[i] = int(x[i].replace('x',''))
            
    C = str(sum(c)) if str(sum(c)) != '0' else ''
    plus = ' + ' if C else ''
    X = ''
    if sum(x) == 1:
        X = 'x'
    elif sum(x) == 0:
        X = ''
        plus = ''
    else:
        X = str(sum(x)) + 'x'
    return X + plus + C
