def solution(myString, pat):
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'A':
            myString[i] = 'B'
        else:
            myString[i] = 'A'
            
    myString = ''.join(myString)
    
    return 1 if pat in myString else 0

# pat을 바꾸는 풀이
def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)
