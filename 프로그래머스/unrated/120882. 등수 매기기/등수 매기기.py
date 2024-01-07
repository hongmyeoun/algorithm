def solution(score):
    avg = [sum(i)/2 for i in score]
    avg_sort = sorted(avg, reverse=True)
    rank = [avg_sort.index(i)+1 for i in avg]
    return rank