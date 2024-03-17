#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        lengt = len(sentence)
    else:
        lengt = 0
    return (lengt, sentence if not sentence else sentence[0])
