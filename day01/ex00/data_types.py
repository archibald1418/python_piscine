#!/usr/bin/env python3

def data_types():

    a = 0
    b = ''
    c = 0.0
    d = True
    e = []
    f = dict()
    g = tuple()
    h = set()

    vars = [
        a, b, c, d, e, f, g, h
    ]

    types = list(map(lambda x: type(x).__name__, vars))
    print('[', end='')
    for t in range(len(types) - 1):
        print(types[t], end=', ')
    print(types[t], end=']')

if __name__ == '__main__':
    data_types()