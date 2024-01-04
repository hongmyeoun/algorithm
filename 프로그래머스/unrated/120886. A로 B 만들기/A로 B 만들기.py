def solution(before, after):
    before = sorted([c for c in before])
    after = sorted([c for c in after])
    
    return 1 if before == after else 0