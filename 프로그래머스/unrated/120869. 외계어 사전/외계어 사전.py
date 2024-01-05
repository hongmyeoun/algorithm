def solution(spell, dic):
    count = 0
    for c in dic:
        for s in spell:
            if s in c:
                count += 1
        if count >= len(spell):
            return 1
        else:
            count = 0
            
    if count == 0:
        return 2