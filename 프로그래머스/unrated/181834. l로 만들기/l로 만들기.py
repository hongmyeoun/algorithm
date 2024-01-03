def solution(myString):
    forward_i = ["a","b","c","d","e","f","g","h","i","j","k"]
    for c in myString:
        if c in forward_i:
            myString = myString.replace(c,"l")
    return myString