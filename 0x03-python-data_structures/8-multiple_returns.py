#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_i = ()
    if sentence == 0:
        return 'None'
    else:
        tuple_i = len(sentence), sentence[0]
    return tuple_i
