#!/usr/bin/python3
def multiple_returns(sentence):
    lengthofsentence = len(sentence)
    if sentence is None:
        firstletter = None
        return lengthofsentence, firstletter
    firstletter = sentence[0]
    return lengthofsentence, firstletter
