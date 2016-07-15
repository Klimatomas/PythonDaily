#!/usr/bin/env py
for i in open('key.csv', 'r').read().split(","):
    print ''.join(x[0] for x in open('declaration.txt', 'r').read().split(" "))[int(i) - 1],
