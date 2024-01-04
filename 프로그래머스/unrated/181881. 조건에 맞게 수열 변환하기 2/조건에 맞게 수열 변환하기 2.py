def solution(arr):
    x = 0
    result = arr
    while True:
        result_before = result
        result = [] 
        for i in result_before:
            if i >= 50 and not i%2:
                result.append(i/2)
            elif i < 50 and i%2:
                result.append(i*2+1)
            else:
                result.append(i)
                
        if result_before == result:
            break
            
        x += 1
    return x