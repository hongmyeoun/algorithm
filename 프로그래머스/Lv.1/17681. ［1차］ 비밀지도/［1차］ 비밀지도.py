def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []
    
    for i,j in zip(arr1, arr2):
        bin_arr1.append(bin_str_gen(i, n))
        bin_arr2.append(bin_str_gen(j, n))
        
    result = ''
    answer = []
    for i, j in zip(bin_arr1, bin_arr2):
        for c, s in zip(i, j):
            if c == '1' or s == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
        result = ''
        
    return answer

def bin_str_gen(dec, repeat):
    bin_str = ''
    for _ in range(repeat):
        bin_str = str(dec%2) + bin_str
        dec //= 2
    return bin_str

# rjust와 bin(a|b)
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

bin(a|b)는 a와 b를 or로 계산해서 새로운 이진수를 만들어냄 -> [2:] 이걸로 앞 0b를 제거한 str생성
rjust(n,'0') -> n에 맞게 우측으로 정렬후 빈공간(좌측)을 '0'으로 채움
