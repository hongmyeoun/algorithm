def solution(myString, pat):
    idx = myString.rfind(pat)
    return myString[:idx + len(pat)] if idx != -1 else myString