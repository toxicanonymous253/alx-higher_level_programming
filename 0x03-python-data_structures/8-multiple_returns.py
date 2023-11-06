#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0, None
    else:
        lengthofsentence = len(sentence)
        firstletter = sentence[0]
        return lengthofsentence, firstletter
