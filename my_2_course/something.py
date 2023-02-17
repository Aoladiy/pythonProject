abc = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


def duplicate_encode(word):
    word = word.lower()
    s = {x: word.count(x) for x in [verb for verb in word]}
    for key in s.keys():
        if key in abc:
            word = word.replace(key, '(')
        if s[key] != 1:
            word = word.replace(key, ')')
        if s[key] == 1:
            word = word.replace(key, '(')
    return word
