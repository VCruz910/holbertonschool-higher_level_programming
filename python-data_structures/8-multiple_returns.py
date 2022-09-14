#!/usr/bin/python3
def multiple_returns(sentence):
    SenLen = len(sentence)

    if (SenLen == 0):
        NTuple = (SenLen, None)
    else:
        NTuple = (SenLen, sentence[0])
    return (NTuple)
