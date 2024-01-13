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