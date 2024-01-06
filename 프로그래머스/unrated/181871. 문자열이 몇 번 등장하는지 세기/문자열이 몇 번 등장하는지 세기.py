def solution(myString, pat):
    count = 0
    start_index = 0
    while True:
        index = myString.find(pat, start_index)
        
        if index == -1:
            break
        
        start_index = index + 1
        
        count += 1
        
    return count