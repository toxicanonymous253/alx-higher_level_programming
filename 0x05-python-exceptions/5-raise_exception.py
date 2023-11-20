#!/usr/bin/python3
def raise_exception():
    a = "h"
    b = 2
    try:
        answer = a + b
        return answer
    except TypeError:
        raise TypeError
