def prefixs(word):
    if len(word) > 0:
        yield from prefixs(word[:-1])
        yield word
def postfixs(word):
    if len(word) > 0:
        yield word
        yield from postfixs(word[:-1])
    