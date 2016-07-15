#!/usr/bin/env python

def is_valid(symbol, element):
    e = list(element.lower())
    s = list(symbol.lower())
    for i in s:
        if i in e:
            e = e[e.index(i):]
        else:
            return False
    return True

is_valid('Er', 'Silver')
is_valid('Zt','Stantzon')