#!/usr/bin/python3
def multiple_returns(sentence):
    senlen = len(sentence)
    if senlen == 0:
        firlet = None
    else:
        firlet = sentence[0]
    tupledata = (senlen, firlet)
    return tupledata
