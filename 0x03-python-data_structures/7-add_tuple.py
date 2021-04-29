#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        fira = tuple_a[0]
        if len(tuple_a) >= 2:
            seca = tuple_a[1]
        else:
            seca = 0
    else:
        fira = 0
        seca = 0
    if len(tuple_b) >= 1:
        firb = tuple_b[0]
        if len(tuple_b) >= 2:
            secb = tuple_b[1]
        else:
            secb = 0
    else:
        firb = 0
        secb = 0
    firsum = fira + firb
    secsum = seca + secb
    sumtuple = (firsum, secsum)
    return sumtuple
