def solution(rank, attendance):
    true_rank = []
    d = dict(zip(rank, attendance))
    for key in d.keys():
        if d[key]:
            true_rank.append(key)
    
    true_rank.sort()

    return 10000*rank.index(true_rank[0]) + 100*rank.index(true_rank[1]) + rank.index(true_rank[2])

# enumerate로 풀이
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
