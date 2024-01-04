def solution(emergency):
    em_dict = dict(zip(sorted(emergency, reverse=True), list(range(1,len(emergency)+1))))
    return [em_dict[i] for i in emergency]