def solution(before, after):
    before = sorted([c for c in before])
    after = sorted([c for c in after])
    
    return 1 if before == after else 0

# str을 sorted를 하면 굳이 list를 만들 필요가 없음
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
